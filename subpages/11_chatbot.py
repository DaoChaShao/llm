from streamlit import chat_input
from streamlit_chat import message

message(
    "Hello, how are you?",
    is_user=False,
    avatar_style="pixel-art",
    allow_html=True,
    is_table=True
)

prompt: str = chat_input("Send a message...", max_chars=100)
