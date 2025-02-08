from streamlit import title, divider, expander, caption, empty

from utilities import subpages_setter


def main():
    """ streamlit run application/main.py """
    title("LLM")
    divider()
    expander("The target of this application", expanded=True)
    caption("1. Download the model from **[ModelScope](https://www.modelscope.cn/)**")

    empty_message = empty()

    subpages_setter()

    # model_name = "qwen/Qwen2.5-7B-Instruct"


if __name__ == "__main__":
    main()
