import os

from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("YA_URL")
KEY = os.getenv("YA_KEY")
headers = {'Authorization': KEY}
