import requests

api_endpoint = 'http://localhost:11434/api/generate'

data = {
    'model' : 'qwen3:1.7b',
    'stream' : False,
    'prompt' : 'Act as a translator. Translate this to Russian: car'
}

response = requests.post(api_endpoint, json=data)

if response.status_code == 200:
    response_data = response.json()
    print(response_data)

else:
    print('Failed to get response from the Ollama API')
    