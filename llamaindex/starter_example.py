# Implementing the LlamaIndex [Starter Tutorial](https://gpt-index.readthedocs.io/en/stable/getting_started/starter_example.html)

from llama_index import VectorStoreIndex, SimpleDirectoryReader
import openai
from dotenv import load_dotenv
import os
import logging
import sys

# Set logging to DEBUG for verbose output
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Load the .env variables and set API key.
load_dotenv() 
openai.api_key = os.getenv("OPENAI_API_KEY")

documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
query = "What did the author do growing up?"
print("Query: %s" % query)
response = query_engine.query("What did the author do growing up?")
print("Response: %s" % response)
