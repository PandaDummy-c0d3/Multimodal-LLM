import requests
import base64

# load image
with open('pandas-closeup.jpg', 'rb') as image_file:

    #1. read it's content (binary)
    image_data = image_file.read()

    #2. turn binary into base 64
    base64_image = base64.b64encode(image_data)

    #3. encode to utf-8
    base64_image_string = base64_image.decode('utf-8')


api_endpoint = 'http://localhost:11434/api/generate'

data = {
    'model' : 'llava-phi3:latest',
    'stream' : False,
    'prompt' : 'Describe the image provided',
    'images' : [base64_image_string]
}

response = requests.post(api_endpoint, json=data)

if response.status_code == 200:
    response_data = response.json()
    print(response_data['response'])

else:
    print('Failed to get response from the Ollama API')
    