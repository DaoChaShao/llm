from modelscope import snapshot_download
from PIL import Image, ImageDraw, ImageFont
from streamlit import (Page, navigation, sidebar, header, selectbox,
                       text_area, empty, image)
from textwrap import wrap


def subpages_setter() -> None:
    """ Set the subpages on the sidebar """
    pages: dict = {
        "page": [
            "subpages/1_home.py",
            "subpages/2_models.py",
            "subpages/3_title2images.py",
            "subpages/4_content2images.py",
        ],
        "title": ["Home", "Model Download", "Title to Image Transfer", "Content to Image Transfer"],
        "icon": [":material/home:", ":material/download:", ":material/photo_library:", ":material/image:"],
    }

    page_structure: dict = {
        "Introduction": [
            Page(page=pages["page"][0], title=pages["title"][0], icon=pages["icon"][0]),
        ],
        "Actions": [
            Page(page=pages["page"][1], title=pages["title"][1], icon=pages["icon"][1]),
            Page(page=pages["page"][2], title=pages["title"][2], icon=pages["icon"][2]),
            Page(page=pages["page"][3], title=pages["title"][3], icon=pages["icon"][3]),
        ],
    }
    pg = navigation(page_structure, position="sidebar", expanded=True)
    pg.run()


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


def content2images_params() -> dict:
    """ Set and get parameters for content to images """
    parameters: dict = {}
    with sidebar:
        header("Parameters")
        options: list = [300, 400, 500, 600]
        zone_height: int = sidebar.slider(
            "Zone Height", min_value=300, max_value=600, value=300, step=100, format="%d",
            help="Adjust the height of the text zone."
        )
        parameters["zone_height"]: int = zone_height
        content_max: int = sidebar.slider(
            "Content Max Length", min_value=100, max_value=900, value=300, step=100, format="%d",
            help="Before your enter, adjust the size of the content zone FIRSTLY."
        )
        parameters["content_max"]: int = content_max
        content_size: int = sidebar.slider(
            "The Font Size of Your Content", min_value=12, max_value=36, value=16, step=2, format="%d",
            help="Before your enter, adjust the size of the content zone FIRSTLY."
        )
        parameters["font_size"]: int = content_size

    return parameters


def text2images_setter(text: str, message: empty):
    """ Transferring text to images """
    options_box: list[str] = ["Wei Xiao", "Happy", "Cao"]
    font_selected: str = sidebar.selectbox(
        "Font", ["Select"] + options_box, placeholder="Select a font",
        help="Choose a font for the title."
    )
    match font_selected:
        case "Wei Xiao":
            font_selected: str = "fonts/ZCOOLXiaoWei-Regular.ttf"
        case "Happy":
            font_selected: str = "fonts/ZCOOLKuaiLe-Regular.ttf"
        case "Cao":
            font_selected: str = "fonts/LiuJianMaoCao-Regular.ttf"
        case _:
            message.error("Please select a font.")

    font_size: int = sidebar.slider(
        "The Font Size of Your Title", min_value=100, max_value=240, value=168, step=2, format="%d",
        help="Adjust the fonts size of your content."
    )
    options_seg: list[str] = ["Horizontal", "Squarish", "Vertical"]
    layout: str = sidebar.segmented_control(
        "Image Layout", options_seg, default="Horizontal", selection_mode="single",
        help="Choose the layout of the images."
    )
    line_space: int = sidebar.slider(
        "Line Space", min_value=30, max_value=60, value=36, step=2, format="%d",
        help="Adjust the space between the title and the content."
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
            image_generator(text, font_selected, font_size, line_space, color_font, color_bg, image_width, image_height)
            message.success("Images generated successfully.")
        else:
            message.info("Now you can push the button to generate images.")
    else:
        message.warning("Please select the layout of the images.")


def image_generator(
        text: str, font_selected: str, font_size: int, text_line_space: int, color_font: str, color_bg: str, width: int,
        height: int):
    """ Generate images based on input """
    from PIL import Image, ImageDraw, ImageFont
    import textwrap

    # Set up fonts
    font = ImageFont.truetype(font_selected, font_size, encoding="utf-8")

    img: Image = Image.new("RGB", (width, height), color_bg)
    draw = ImageDraw.Draw(img)

    # Calculate the max number of characters in each line
    char_width: float = font.getbbox("中")[2]  # Single Chinese character width
    max_chars_per_line: int = int(width // char_width)  # How many characters fit in one line

    # Wrap text
    wrapped_text: list[str] = textwrap.wrap(text, width=max_chars_per_line)

    # Calculate the height of each line
    line_height: float = font.getbbox("中")[3] - font.getbbox("中")[1] + text_line_space

    # Calculate the starting position of the text
    y_start = max(50, int((height - len(wrapped_text) * line_height) // 2))

    # Draw the text on the image with better centering
    y_offset = y_start
    for line in wrapped_text:
        text_width = font.getlength(line)  # Get the actual width of the whole line
        x_start = (width - text_width) // 2  # Center horizontally

        draw.text((x_start, y_offset), line, fill=color_font, font=font)
        y_offset += line_height

    image(img, output_format="PNG", use_container_width=True)
