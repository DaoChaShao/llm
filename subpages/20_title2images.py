from streamlit import title, divider, text_input, empty

from utilis.red_note import text2images_setter

title("Title to Images")
divider()

empty_message: empty = empty()

TITLE_LENGTH: int = 30
title_text: str = text_input(
    "Title", max_chars=TITLE_LENGTH, placeholder="Enter a title here", type="default",
    help="Create a title for your content here."
)

if title_text:
    text2images_setter(title_text, empty_message)

else:
    empty_message.error("Please enter a title for your content.")
