**The instructions for using the ModelScope model**
---
1. This application is a simple implementation of setting down an LLM locally.
2. Put the downloaded model into the Ollama client with `ollama create model_name -f Modelfile`
3. If you want to remove the model from the Ollama client, use `ollama rm model_name`
4. If you want to use the model that has been added to the Ollama client, use `ollama run model_name`
5. If you want to use `from modelscope import AutoModelForCausalLM, AutoTokenizer` to load the download model,  
   you should `pip install transformers` first. Otherwise, the error will occur.

**The instructions for using the Milvus**  
1. Milvus is used to conduct vectors, such as save, query search, and other operations.
2. If you want to use Milvus, you should install it first with the command `pip install pymilvus`.

**Resources**
---
Deploy, manage and share your apps for free using our [Community Cloud](https://streamlit.io/cloud)!   
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://llm-com.streamlit.app/)

**License**
---
[BSD 3-Clause](LICENSE)
