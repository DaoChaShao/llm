from streamlit import title, divider, text_input, sidebar, markdown, empty

from utilities import zone_text, text2images_setter

title("Text2Images")
divider()

empty_message: empty = empty()

TITLE_LENGTH: int = 30
title_text: str = text_input(
    "Title", max_chars=TITLE_LENGTH, placeholder="Enter a title here", type="default",
    help="Create a title for your content here."
)

if title_text:
    options: list = [300, 400, 500, 600]
    zone_height: int = sidebar.slider(
        "Zone Height", min_value=300, max_value=600, value=300, step=100, format="%d",
        help="Adjust the height of the text zone."
    )
    content_max: int = sidebar.slider(
        "Content Max Length", min_value=100, max_value=900, value=300, step=100, format="%d",
        help="Before your enter, adjust the size of the content zone FIRSTLY."
    )
    content_text: str = zone_text(zone_height, content_max)
    title_size: int = sidebar.slider(
        "The Font Size of Your Title", min_value=100, max_value=240, value=168, step=2, format="%d",
        help="Adjust the fonts size of your content."
    )
    content_size: int = sidebar.slider(
        "The Font Size of Your Content", min_value=12, max_value=36, value=16, step=2, format="%d",
        help="Before your enter, adjust the size of the content zone FIRSTLY."
    )
    sidebar.divider()

    if content_text.strip():
        text2images_setter(title_text, title_size, content_text, content_size, empty_message)

    else:
        empty_message.error("Please enter content for your text zone.")
else:
    empty_message.error("Please enter a title for your content.")
