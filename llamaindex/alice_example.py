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

# Index / embed the custom data 
documents = SimpleDirectoryReader('data_alice').load_data()
index = VectorStoreIndex.from_documents(documents)

# Query
query_engine = index.as_query_engine()
query = "What does Alice look like?"
response = query_engine.query(query)

# Report results
print("Query: %s" % query)
print("Response: %s" % response)

query = "How does Alice get down the hole?"
response = query_engine.query(query)
print("Query: %s" % query)
print("Response: %s" % response)


query = "Who is at the tea party?"
response = query_engine.query(query)
print("Query: %s" % query)
print("Response: %s" % response)


query = "Write a short paragraph to describe the tea party."
response = query_engine.query(query)
print("Query: %s" % query)
print("Response: %s" % response)
