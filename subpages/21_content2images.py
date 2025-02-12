from streamlit import title, divider, text_area, empty

from utilities.red_note import content2images_params, text2images_setter

title("Content to Images")
divider()

empty_message: empty = empty()

params: dict = content2images_params()

content = text_area(
    "Content", placeholder="Type something here", height=params["zone_height"], max_chars=params["content_max"],
    help="This is a text area. Before your enter, adjust the size of the content zone FIRSTLY."
)

if content.strip():
    text2images_setter(content, empty_message)

else:
    empty_message.error("Please enter content for your text zone.")
