from streamlit import text_input, sidebar, markdown, empty

from utilities import zone_text, text2images_setter

empty_message: empty = empty()

TITLE_LENGTH: int = 30
title: str = text_input(
    "Title", max_chars=TITLE_LENGTH, placeholder="Enter a title here", type="default",
    help="Create a title for your content here."
)

if title:
    title_level: int = sidebar.slider(
        "Font Size", min_value=1, max_value=6, value=3, step=1, format="%d",
        help="Adjust the font size of your content."
    )
    options: list = [300, 400, 500, 600]
    zone_height: int = sidebar.slider(
        "Zone Height", min_value=300, max_value=600, value=300, step=100, format="%d",
        help="Adjust the height of the text zone."
    )
    content_length: int = sidebar.slider(
        "Content Size", min_value=100, max_value=900, value=300, step=100, format="%d",
        help="Before your enter, adjust the size of the content zone FIRSTLY."
    )
    content: str = zone_text(zone_height, content_length)

    if content:
        markdown(f"{'#' * title_level} {title}")
        markdown(content)
        text2images_setter(title, TITLE_LENGTH, empty_message)

    else:
        empty_message.error("Please enter content for your text zone.")
else:
    empty_message.error("Please enter a title for your content.")
