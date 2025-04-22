import requests
import os
import logging
from dotenv import load_dotenv, dotenv_values
from setting import DOT_ENV_DIR, LOGGER_DIR

load_dotenv(DOT_ENV_DIR)
os.getenv("NEWS_API")

# logger conf
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(LOGGER_DIR)
stream_handler = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")

file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)




class APIHandler:
    def __init__(self, api: str):
        self.api = api
        self.status_code = None
        self.content = None

    def get_req(self):
        response = requests.get(self.api)
        self.status_code = response.status_code
        self.content = response.json()
        logger.info(f"get request status code: {self.status_code}")


api_handler = APIHandler(os.getenv("NEWS_API"))
# api_handler.get_req()

# # print(api_handler.status_code,"\n",api_handler.content)

