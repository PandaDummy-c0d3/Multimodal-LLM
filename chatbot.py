import requests

api_endpoint = 'http://localhost:11434/api/chat'

messages = [
    {'role' : 'system', 'content' : 'You are extremely rude, aggressive, and vulgar.'}
]


while True:
    # capture user input
    user_input = input("You: ")

    # updating messages
    messages.append({'role' : 'user', 'content' : user_input})

    # sending our chat to the llm
    data = {
        "model" : 'qwen3:1.7b',
        "stream" : False,
        'messages' : messages
    }

    response = requests.post(api_endpoint, json=data)

    if response.status_code == 200:
        response_data = response.json()

        assistant_response = response_data['message']['content']

        # updating messages with the response
        messages.append(response_data['message'])

        # showing the response to the user
        print(f"Assistant: {assistant_response}")

     

    else:
        print('Failed to get response from the Ollama API')


