import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path
import os

def send_text_prompt(prompt):
    dotenv_path = Path("environment.env")
    load_dotenv(dotenv_path=dotenv_path)

    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    response = model.generate_content(prompt)
    return response.text
