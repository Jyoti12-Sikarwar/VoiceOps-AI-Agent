import os
import google.generativeai as genai
from dotenv import load_dotenv

# API Key Setup (Secured)
load_dotenv() 
my_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=my_api_key)