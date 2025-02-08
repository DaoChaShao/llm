from modelscope import snapshot_download
from streamlit import Page, navigation, sidebar, header, selectbox


def subpages_setter() -> None:
    """ Set the subpages on the sidebar """
    subpage_pages: list = ["subpages/home.py", "subpages/models.py"]
    subpage_titles: list = ["Home", "Model Download"]
    subpage_icons: list = [":material/home:", ":material/download:"]

    subpages: dict = {
        "Introduction": [
            Page(page=subpage_pages[0], title=subpage_titles[0], icon=subpage_icons[0]),
        ],
        "Actions": [
            Page(page=subpage_pages[1], title=subpage_titles[1], icon=subpage_icons[1]),
        ],
    }
    pages = navigation(subpages)
    pages.run()


def sidebar_params_download():
    parameters = {}

    with sidebar:
        header("Parameters")
        models: list = ["qwen/Qwen2.5-7B-Instruct", ]
        model_name = selectbox("Model Name", ["Select"] + models)
        if model_name != "Select":
            parameters["model_name"] = model_name

    return parameters


def scope_model_downloader(model_name: str):
    model_dir = snapshot_download("Qwen/Qwen2.5-0.5B-Instruct")
