from streamlit import Page, navigation


def subpages_setter() -> None:
    """ Set the subpages on the sidebar """
    pages: dict = {
        "page": [
            "subpages/00_home.py",
            "subpages/10_models.py",
            "subpages/11_chatbot.py",
            "subpages/12_knowledge_base.py",
            "subpages/20_title2images.py",
            "subpages/21_content2images.py",
        ],
        "title": [
            "Home",
            "Model Download",
            "ChatBot",
            "Knowledge Base",
            "Title to Image Transfer",
            "Content to Image Transfer",
        ],
        "icon": [
            ":material/home:",
            ":material/download:",
            ":material/robot:",
            ":material/book:",
            ":material/photo_library:",
            ":material/image:"
        ],
    }

    page_structure: dict = {
        "Introduction": [
            Page(page=pages["page"][0], title=pages["title"][0], icon=pages["icon"][0]),
        ],
        "LLM Actions": [
            Page(page=pages["page"][1], title=pages["title"][1], icon=pages["icon"][1]),
            Page(page=pages["page"][2], title=pages["title"][2], icon=pages["icon"][2]),
            Page(page=pages["page"][3], title=pages["title"][3], icon=pages["icon"][3]),
        ],
        "Red Note": [
            Page(page=pages["page"][4], title=pages["title"][4], icon=pages["icon"][4]),
            Page(page=pages["page"][5], title=pages["title"][5], icon=pages["icon"][5]),
        ],
    }
    pg = navigation(page_structure, position="sidebar", expanded=True)
    pg.run()
