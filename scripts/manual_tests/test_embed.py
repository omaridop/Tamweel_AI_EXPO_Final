from openai import OpenAI
import os
client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)
try:
    resp = client.embeddings.create(model="google/text-embedding-004", input=["Hello world"], encoding_format="float")
    print(resp.data[0].embedding[:5])
except Exception as e:
    print("google/text-embedding-004", repr(e))

try:
    resp = client.embeddings.create(model="text-embedding-004", input=["Hello world"], encoding_format="float")
    print(resp.data[0].embedding[:5])
except Exception as e:
    print("text-embedding-004", repr(e))

try:
    resp = client.embeddings.create(model="text-embedding-3-small", input=["Hello world"], encoding_format="float")
    print(resp.data[0].embedding[:5])
except Exception as e:
    print("text-embedding-3-small", repr(e))
