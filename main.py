import pickle
from news.api_handler import APIHandler
from utils.context_manager import PickleContextManager
from setting.directories import NEWS_DATA_DIR
from setting.argument_processor import Argument


# config args
args_handler = Argument()
dict_args = args_handler.get_dict_args()

#init api handlers
api_handler = APIHandler()


#sending GET request
api_handler.get_req(api=args_handler.raw_url, params=args_handler.dict_args)
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
