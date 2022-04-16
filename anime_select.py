import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv('URL')

headers = {"Content-Type" : "application/json", "Accept" : "text/plain"}

response = requests.post(base_url, data="mal.json", headers=headers)
print(response.status_code)