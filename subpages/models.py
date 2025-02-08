from streamlit import title, divider, expander, caption, empty

from utilities import sidebar_params_download

title("Model Download")
divider()
with expander("Model Download", expanded=True):
    caption("This page is designed to download the model from **[ModelScope](https://www.modelscope.cn/)**.")

empty_message = empty()

# Set the sidebar parameters
parameters = sidebar_params_download()
