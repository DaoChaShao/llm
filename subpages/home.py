from streamlit import title, divider, expander, caption, empty

title("LLM Application")
divider()
with expander("The Application Introduction", expanded=True):
    caption("This application is designed to practice setting, modifying, and ragging the LLM model.")
    caption("1. Download the model from **[ModelScope](https://www.modelscope.cn/)**")

empty_message = empty()
