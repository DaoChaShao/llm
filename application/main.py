from streamlit import title, divider, expander, caption, empty

from utilities import subpages_setter


def main():
    """ streamlit run application/main.py """
    # Set the subpages on the sidebar
    subpages_setter()

    # model_name = "qwen/Qwen2.5-7B-Instruct"


if __name__ == "__main__":
    main()
