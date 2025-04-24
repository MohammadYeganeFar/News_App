import logging
import os
from setting.directories import CONTEXT_MGR_LOG_DIR

def create_file_if_not_exist(path):
    open(path, "a")

create_file_if_not_exist(CONTEXT_MGR_LOG_DIR)

utils_logger = logging.getLogger(__name__,)
utils_formatter = "%(asctime)s:%(name)s:%(levelname)s:%(message)s"
logging.basicConfig(filename=CONTEXT_MGR_LOG_DIR,
                    format=utils_formatter,
                    level=10)



def setup_logger(*, f_path, file_handler_level:int=10,
                  stream_handler_level:int=10,
                  frmt=None,
                  name:str):

    if not os.path.exists(f_path):
        create_file_if_not_exist(f_path)
        utils_logger.info(f"file not found. now created: {f_path}")


    if frmt is None:
        frmt = "%(asctime)s:%(name)s:%(levelname)s:%(message)s"

    if name is None:
        raise NameError("put a __name__")
    my_logger = logging.getLogger(name)
    my_logger.setLevel(10)

    file_handler = logging.FileHandler(f_path)
    formatter = logging.Formatter(frmt)

    file_handler.setLevel(file_handler_level)
    file_handler.setFormatter(formatter)
    my_logger.addHandler(file_handler)

    # bug: stream_handler
    # stream_handler.setLevel(stream_handler_level)
    # stream_handler.setFormatter(frmt)
    # stream_handler = logging.StreamHandler()
    # my_logger.addHandler(stream_handler)

    return my_logger


