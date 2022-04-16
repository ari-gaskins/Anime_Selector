import requests
import os
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv('URL')

response = requests.get(URL)
print(response.status_code)