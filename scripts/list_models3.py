import os
import requests

api_key = "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"
response = requests.get("https://openrouter.ai/api/v1/models")
data = response.json()
count = 0
for m in data.get('data', []):
    name = m['id']
    print(name)
    count += 1
print('Total models:', count)
