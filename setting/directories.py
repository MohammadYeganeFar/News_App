from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = Path.joinpath(BASE_DIR, "data")

CONTEXT_MGR_LOG_DIR = Path.joinpath(DATA_DIR, "logs/context_manager.log")
REQUESTS_LOG_DIR = Path.joinpath(DATA_DIR, "logs/requests.log")
NEWS_DATA_DIR = Path.joinpath(DATA_DIR, "news_data.pkl")
LAST_UPDATE_OF_CACHE = Path.joinpath(DATA_DIR, "last_update.txt")

DOT_ENV_DIR = Path.joinpath(BASE_DIR, ".env")