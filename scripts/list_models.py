import os
import requests

api_key = "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"
response = requests.get("https://openrouter.ai/api/v1/models")
data = response.json()
for m in data.get('data', []):
    name = m['id']
    if 'embed' in name.lower() or 'google' in name.lower() or 'gemini' in name.lower():
        print(name)
