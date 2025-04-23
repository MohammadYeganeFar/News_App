import os
import logging
import pickle
from dotenv import load_dotenv
from news.api_handler import APIHandler
from context_manager import PickleContextManager
from setting import NEWS_DATA_DIR, REQUESTS_LOG_DIR
from utils import setup_logger


# loading evnierments
load_dotenv()
news_api = os.getenv("NEWS_API")

#init handlers
api_handler = APIHandler(news_api)

# logger conf logger = setup_logger(f_path=)


#sending GET request
api_handler.get_req()
status_code = api_handler.status_code

if api_handler.status_code == 200:
    # writing into file "news_data.pkl"
    with PickleContextManager(NEWS_DATA_DIR, "wb") as file:
        pickle.dump(api_handler.content, file)
        print(f"GET ok: code {status_code}")

    # reading from file "news_data.pkl"
    with PickleContextManager(NEWS_DATA_DIR, "rb") as file:
        file_content = pickle.load(file)
        for article in file_content["articles"]:
            print(f"--------\ntitle: {article["title"]}\nurl: {article["url"]}")
else:
    print(f"GET failed: code {status_code}")
