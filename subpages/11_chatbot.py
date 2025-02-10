from streamlit import (chat_input, sidebar, header, selectbox, caption,
                       text_input)
from streamlit_chat import message

with sidebar:
    header("Model Selection")
    options: list[str] = ["Online", "Offline"]
    option: str = selectbox(
        "Select a model", ["Select"] + options, placeholder="Select a model",
        help="Select a model to use for text generation"
    )
    if option in options:
        match option:
            case "Online":
                caption("Using the deepseek api key to access the model")
                api_key: str = text_input("Enter the API key", value="", type="password", max_chars=36)
                if api_key:
                    # TODO: call the deepseek api to get the model
                    pass
            case "Offline":
                caption("Using the local model for text generation")

message(
    "Hello, how are you?",
    is_user=False,
    avatar_style="pixel-art",
    allow_html=True,
    is_table=True
)

prompt: str = chat_input("Send a message...", max_chars=100)
