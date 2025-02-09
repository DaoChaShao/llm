from modelscope import snapshot_download
from streamlit import (Page, navigation, sidebar, header, selectbox,
                       text_area, empty)


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


def zone_text(zone_height: int = 300, content_size: int = 300) -> str:
    """ Create a text area for inputting text """
    input_text = text_area(
        "Content", placeholder="Type something here", height=zone_height, max_chars=content_size,
        help="This is a text area. Before your enter, adjust the size of the content zone FIRSTLY."
    )
    return input_text


def text2images_setter(text: str, length: int, message: empty):
    """ Transferring text to images """
    options: list[str] = ["Horizontal", "Squarish", "Vertical"]
    layout: str = sidebar.segmented_control(
        "Image Layout", options, default="Horizontal", selection_mode="single",
        help="Choose the layout of the images."
    )
    if layout:
        match layout:
            case "Horizontal":
                image_width: int = 1080
                image_height: int = 1440
                sidebar.caption(f"Horizontal layout (3:4): {image_width} x {image_height} px.")
            case "Squarish":
                image_width: int = 1080
                image_height: int = 1080
                sidebar.caption(f"Squarish layout (1:1): {image_width} x {image_height} px.")
            case "Vertical":
                image_width: int = 1280
                image_height: int = 720
                sidebar.caption(f"Vertical layout (16:9): {image_width} x {image_height} px.")

        if sidebar.button(
                "Generate Images", on_click=None, args=None, kwargs=None, disabled=False,
                help="Click to generate images."
        ):
            pass
    else:
        message.warning("Please select the layout of the images.")
