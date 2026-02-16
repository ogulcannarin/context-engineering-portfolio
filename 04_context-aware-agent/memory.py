import chromadb
from openai import OpenAI
import uuid
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = chromadb.Client()
collection = client.get_or_create_collection("memory")

openai_client = OpenAI()

def add_memory(text: str):
    emb = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    ).data[0].embedding

    collection.add(
        ids=[str(uuid.uuid4())],
        embeddings=[emb],
        documents=[text]
    )

def search_memory(query: str):
    emb = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    ).data[0].embedding

    results = collection.query(
        query_embeddings=[emb],
        n_results=3
    )

    return results["documents"][0]
