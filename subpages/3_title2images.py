from streamlit import title, divider, text_input, sidebar, empty

from utilities import text2images_setter

title("Title to Images")
divider()

empty_message: empty = empty()

TITLE_LENGTH: int = 30
title_text: str = text_input(
    "Title", max_chars=TITLE_LENGTH, placeholder="Enter a title here", type="default",
    help="Create a title for your content here."
)

if title_text:
    title_size: int = sidebar.slider(
        "The Font Size of Your Title", min_value=100, max_value=240, value=168, step=2, format="%d",
        help="Adjust the fonts size of your content."
    )

    text2images_setter(title_text, title_size, empty_message)

else:
    empty_message.error("Please enter a title for your content.")
