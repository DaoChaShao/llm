from stqdm import stqdm
from streamlit import title, divider, expander, caption, empty, sidebar, spinner

from utilities import sidebar_params_download, scope_model_downloader

title("Model Download")
divider()
with expander("Model Download", expanded=True):
    caption("This page is designed to download the model from **[ModelScope](https://www.modelscope.cn/)**.")

empty_message = empty()

# Set the sidebar parameters
parameters = sidebar_params_download()
if parameters:
    if sidebar.button("Download Model", help="Click to download the model"):
        with stqdm(desc="Downloading the model...", miniters=1.0):
            with spinner("Downloading the model..."):
                scope_model_downloader(parameters["model_name"])
