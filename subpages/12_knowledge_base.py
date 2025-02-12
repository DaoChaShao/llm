# from streamlit import title, divider, empty

from utilities.llm import MilvusDB

# title("Local Knowledge Base")
# divider()
#
# empty_message = empty()

SCHEMA: str = "default"
with MilvusDB(SCHEMA) as milvus_db:
    ...
print(milvus_db)
