import requests
import os
import logging
from dotenv import load_dotenv, dotenv_values
from setting import DOT_ENV_DIR, REQUESTS_LOG_DIR
from utils import setup_logger

load_dotenv(DOT_ENV_DIR)
os.getenv("NEWS_API")

# logger conf
logger = setup_logger(f_path=REQUESTS_LOG_DIR,
                        name=__name__)



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

