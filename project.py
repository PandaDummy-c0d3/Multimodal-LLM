import requests  # noqa: I001
import base64
import csv
import os


def read_image_base64_utf8(file_path):
    # load image
    with open(file_path, 'rb') as image_file:

        #1. read it's content (binary)
        image_data = image_file.read()

        #2. turn binary into base 64
        base64_image_data = base64.b64encode(image_data)

        #3. encode to utf-8
        base64_image_string = base64_image_data.decode('utf-8')

    return base64_image_string

def run_api_call(base64_string):
    api_endpoint = 'http://localhost:11434/api/generate'

    data = {
        'model' : 'llava-phi3:latest',
        'stream' : False,
        'prompt' : 'Output the name of the bird in the image provided and nothing else.',
        'images' : [base64_string]
    }

    response = requests.post(api_endpoint, json=data)

    if response.status_code == 200:
        response_data = response.json()
        print(response_data['response'])
        return response_data['response']

    else:
        print('Failed to get response from the Ollama API')
        return None





with open('bird_description.csv', mode = 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Filename', 'Bird Name' ])

    for filename in os.listdir('birds'):
        if filename.endswith('.jpg'):
            image_string = read_image_base64_utf8(f'birds/{filename}')
            description = run_api_call(image_string)

            writer.writerow([filename, description])