from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = Path.joinpath(BASE_DIR, "data")
LOGGER_DIR = Path.joinpath(BASE_DIR, "data/logger.log")
# NEWS_DATA_DIR = Path.joinpath(BASE_DIR, "data/news_data.txt")
LAST_UPDATE_OF_CACHE = Path.joinpath(BASE_DIR, "data/last_update.txt")

DOT_ENV_DIR = Path.joinpath(BASE_DIR, ".env")