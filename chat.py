import json
import os
import questionary
import requests

def invokeOpenAiAPI(text):
    # Set the API key
    api_key = os.getenv("OPENAI_API_KEY", default=None)
    if not api_key:
        raise Exception("api key is: " + str(api_key))
    # Set the API endpoint
    endpoint = "https://api.openai.com/v1/chat/completions"
    # Set the headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    # Set the data
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": text
            }
        ]
    }

    # Make the request
    return requests.post(endpoint, headers=headers, json=data)

def main():
    while True:
        text = questionary.text("Send a Message:").ask()
        if not text:
            print("AI ChatBot: Bye!")
            exit()
        print("AI ChatBot: Thinking...")
        response = invokeOpenAiAPI(text)
        res = json.loads(response.content.decode("utf8"))
        if not res.get("choices"):
            raise ValueError(res)
        print(f'AI ChatBot: {res["choices"][0]["message"]["content"]}')

main()