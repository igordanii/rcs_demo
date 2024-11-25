from vonage import Auth, Vonage
from vonage_messages.models import RcsText
from dotenv import load_dotenv
from pathlib import Path
import os
import requests
import gemini as g

def get_JWT():
    dotenv_path = Path("environment.env")
    load_dotenv(dotenv_path=dotenv_path)
    JWT = os.environ["JWT"]
    return JWT

def send_message(text, to_number):
    headers = {
        "Authorization": "Bearer "+ get_JWT(),
        "Content-Type": "application/json" ,
        "Accept": "application/json" 
    }
    response = requests.post(url="https://api.nexmo.com/v1/messages", json=create_payload(to_number,text), headers=headers)
    print(response.text)
    
def create_payload(to_number,text):
    payload = {
        "message_type": "text",
        "text":text,
        "to": to_number,
        "from": "vonageigor",
        "channel": "rcs"
    }
    return payload