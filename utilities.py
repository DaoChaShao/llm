from modelscope import snapshot_download
from PIL import Image, ImageDraw, ImageFont
from streamlit import (Page, navigation, sidebar, header, selectbox,
                       text_area, empty, image)
from textwrap import wrap


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


def zone_text(zone_height: int = 300, content_max: int = 300) -> str:
    """ Create a text area for inputting text """
    input_text = text_area(
        "Content", placeholder="Type something here", height=zone_height, max_chars=content_max,
        help="This is a text area. Before your enter, adjust the size of the content zone FIRSTLY."
    )
    return input_text


def text2images_setter(title: str, title_size: int, content: str, content_size: int, message: empty):
    """ Transferring text to images """
    options: list[str] = ["Horizontal", "Squarish", "Vertical"]
    layout: str = sidebar.segmented_control(
        "Image Layout", options, default="Horizontal", selection_mode="single",
        help="Choose the layout of the images."
    )
    title_line_space: int = sidebar.slider(
        "Title Line Space", min_value=30, max_value=60, value=36, step=2, format="%d",
        help="Adjust the space between the title and the content."
    )
    content_line_space: int = sidebar.slider(
        "Content Line Space", min_value=1, max_value=10, value=3, step=1, format="%d",
        help="Adjust the space between the content and the next line."
    )
    col_title, col_content = sidebar.columns(2, vertical_alignment="bottom", gap="large")
    color_font: str = col_title.color_picker(
        "Font Color Picker", value="#000000", help="Choose the color of the title."
    )
    color_bg: str = col_content.color_picker(
        "Background Color Picker", value="#FEFEFF", help="Choose the color of the content."
    )

    if layout:
        image_width: int = 0
        image_height: int = 0
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

        if sidebar.button("Generate Images", help="Click to generate images."):
            image_generator(title, title_size, title_line_space, color_font, color_bg, image_width, image_height)
        else:
            message.info("Now you can push the button to generate images.")
    else:
        message.warning("Please select the layout of the images.")


def image_generator(
        text: str, text_size: int, text_line_space: int, color_font: str, color_bg: str, width: int, height: int):
    """ Generate images based on input """
    # Set up fonts
    font_selected: str = "fonts/ZCOOLKuaiLe-Regular.ttf"
    font = ImageFont.truetype(font_selected, text_size, encoding="utf-8")

    img: Image = Image.new("RGB", (width, height), color_bg)
    draw = ImageDraw.Draw(img)

    # Calculate the width of each chinese character
    char_width: float = font.getbbox("中")[2]
    # Calculate the max number of characters in each line
    characters_in_line: int = int(width // char_width)

    wrapped_text: list[str] = wrap(text, width=characters_in_line)

    # Calculate the height of each line
    line_height: float = font.getbbox("中")[3] - font.getbbox("中")[1] + text_line_space

    # Calculate the starting position of the text
    y_start = max(50, int((height - len(wrapped_text) * line_height) // 2))

    # Draw the text on the image
    y_offset = y_start
    for line in wrapped_text:
        draw.text((50, y_offset), line, fill=color_font, font=font)
        y_offset += line_height

    image(img, output_format="PNG", use_container_width=True)
