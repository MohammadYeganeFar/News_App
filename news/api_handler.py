import requests
import os
from dotenv import load_dotenv
from setting.directories import DOT_ENV_DIR, REQUESTS_LOG_DIR
from utils.utils import setup_logger

load_dotenv(DOT_ENV_DIR)
os.getenv("NEWS_API")

# logger conf
logger = setup_logger(f_path=REQUESTS_LOG_DIR,
                        name=__name__)



class APIHandler:
    def __init__(self):

        self.status_code = None
        self.content = None

    def get_req(self, *, api:str, params:dict):
        response = requests.get(api,params=params)
        self.status_code = response.status_code
        self.content = response.json()
        logger.info(f"get request status code: {self.status_code}\nparams: {params}")

        if self.status_code != 200:
            logger.error(f"response: {response.content}")

