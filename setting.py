from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = Path.joinpath(BASE_DIR, "data")

CONTEXT_MGR_LOG_DIR = Path.joinpath(BASE_DIR, "data/logs/context_manager.log")
REQUESTS_LOG_DIR = Path.joinpath(BASE_DIR, "data/logs/requests.log")


NEWS_DATA_DIR = Path.joinpath(BASE_DIR, "data/news_data.pkl")
LAST_UPDATE_OF_CACHE = Path.joinpath(BASE_DIR, "data/last_update.txt")

DOT_ENV_DIR = Path.joinpath(BASE_DIR, ".env")