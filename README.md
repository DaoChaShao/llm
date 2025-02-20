**The instructions for using the ModelScope model**

1. This application is a simple implementation of setting down a LLM locally.
2. Put the downloaded model into the ollama client with `ollama create model_name -f Modelfile`
3. If you want to remove the model from the ollama client, use `ollama rm model_name`
4. If you want to use the model that has been added to the ollama client, use `ollama run model_name`
5. If you want to use `from modelscope import AutoModelForCausalLM, AutoTokenizer` load the download model,  
   you should `pip install transformers` first. Otherwise, error will occur.

**The instructions for using the Milvus**  
1. Milvus is used for conducting vector, such as save, query and search and other operations.
2. If you want to use Milvus, you should install it first with command `pip install pymilvus`.

**License**  
[BSD 3-Clause](LICENSE)
