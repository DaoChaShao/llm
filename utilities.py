from modelscope import snapshot_download
from streamlit import (Page, navigation, sidebar, header, selectbox,
                       text_area)


def subpages_setter() -> None:
    """ Set the subpages on the sidebar """
    subpage_pages: list = ["subpages/home.py", "subpages/models.py", "subpages/text2images.py"]
    subpage_titles: list = ["Home", "Model Download", "Text Transfer"]
    subpage_icons: list = [":material/home:", ":material/download:", ":material/photo_library:"]

    subpages: dict = {
        "Introduction": [
            Page(page=subpage_pages[0], title=subpage_titles[0], icon=subpage_icons[0]),
        ],
        "Actions": [
            Page(page=subpage_pages[1], title=subpage_titles[1], icon=subpage_icons[1]),
            Page(page=subpage_pages[2], title=subpage_titles[2], icon=subpage_icons[2]),
        ],
    }
    pages = navigation(subpages)
    pages.run()


def sidebar_params_download() -> dict:
    parameters = {}

    with sidebar:
        header("Parameters")
        models: list = ["qwen/Qwen2.5-7B-Instruct-GGUF", ]
        model_name = selectbox("Model Name", ["Select"] + models)
        if model_name != "Select":
            parameters["model_name"] = model_name

    return parameters


def scope_model_downloader(model_name: str):
    local_path: str = "models/"
    model_dir = snapshot_download(
        model_name,
        local_dir=local_path,
        revision="master",
        max_workers=8,
    )


def zone_text() -> str:
    input_text = text_area(
        "Content", placeholder="Type something here", height=600,
        help="This is a text area. You can type a lot of text here."
    )
    return input_text
