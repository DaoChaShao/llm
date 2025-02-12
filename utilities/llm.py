from modelscope import snapshot_download, AutoModelForCausalLM, AutoTokenizer
from pymilvus import connections, db
from streamlit import sidebar, header, selectbox, empty, write


def sidebar_params_download(message: empty) -> dict:
    parameters = {}

    with sidebar:
        header("Parameters")
        model_names: list[str] = ["qwen/Qwen2.5-7B-Instruct-GGUF", ]
        model_name = selectbox("Model Name", ["Select"] + model_names)
        if model_name != "Select":
            if model_name == "qwen/Qwen2.5-7B-Instruct-GGUF":
                patterns: list[str] = ["qwen2.5-7b-instruct-q2_k.gguf", "qwen2.5-7b-instruct-q3_k_m.gguf"]
                pattern: str = selectbox("Pattern", ["Select"] + patterns)
                if pattern != "Select":
                    parameters["model_name"] = model_name
                    parameters["file_pattern"] = pattern
                else:
                    message.error("Please select a pattern.")
        else:
            message.error("Please select a model.")

    return parameters


def model_downloader_scope(params: dict) -> None:
    local_path: str = "models/"
    snapshot_download(
        params["model_name"],
        local_dir=local_path,
        revision="master",
        max_workers=8,
        allow_file_pattern=params["file_pattern"],
        ignore_file_pattern=["._____temp", ".msc", ".mv"],
    )


def model_loader_scope(params: dict, sys_content: str, prompt: str) -> str:
    """ Load the local model and tokenizer """
    # Initialize the model
    model = AutoModelForCausalLM.from_pretrained(
        params["model_name"],
        torch_dtype="auto",
        device_map="auto"
    )
    # Initialize the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(params["model_name"])

    messages = [
        {"role": "system", "content": sys_content},
        {"role": "user", "content": prompt}
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=512
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    return tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]


def model_loader_deepseek_api(api_key: str, sys_content: str, prompt: str):
    # TODO: Implement the deepseek API
    pass


def sidebar_params_kb(message: empty) -> None:
    uploaded_files = sidebar.file_uploader(
        "Choose a CSV file", accept_multiple_files=True
    )
    if uploaded_files:
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            write("filename:", uploaded_file.name)
            write(bytes_data)
    else:
        message.error("Please upload a CSV file.")


class MilvusDB(object):
    def __init__(self, schema: str = "default"):
        # self._message = message
        self._schema = schema

    def __enter__(self):
        connections.connect(alias=self._schema, host="localhost", port="19530")
        if db.connections.has_connection(self._schema):
            # self._message.success("Connection established successfully.")
            print("Connection established successfully.")
        else:
            # self._message.error("Connection failed.")
            print("Connection failed.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        connections.disconnect(alias=self._schema)
