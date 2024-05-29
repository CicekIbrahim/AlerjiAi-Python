import os
import base64
import requests

def get_llm_response(base64_image):
    api_key = os.getenv("SECRET_API_KEY")  # your llm api key
    base_url = os.getenv("BASE_URL")  # your llm api base url
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Resimdeki paketli gıda nedir. yalnızca marka ve ürün adını ver başka hiç bir text dönnme!"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ]
    }
    response = requests.post(f"{base_url}", headers=headers, json=data)
    return response.json()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
