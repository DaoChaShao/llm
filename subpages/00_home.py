from streamlit import title, divider, expander, caption, empty

title("Red Note Cover Generator")
divider()
with expander("The Application Introduction", expanded=True):
    caption("This application is designed to practice converting the text to the images.")

empty_message = empty()
