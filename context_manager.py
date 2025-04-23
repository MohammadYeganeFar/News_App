from os import path
import logging
from typing import TextIO
from setting import CONTEXT_MGR_LOG_DIR
from utils import setup_logger

logger = setup_logger(f_path=CONTEXT_MGR_LOG_DIR,
                        name=__name__,
                        )

class PickleContextManager:
    def __init__(self, file_path: str, mode: str) -> None:
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self) -> TextIO:
        if path.exists(self.file_path):
            self.file = open(self.file_path, self.mode)
            logger.info(f"opened file {self.file_path}")
            return self.file
        else:
            raise FileNotFoundError(f"file not found: {self.file_path}")

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        if self.file:
            self.file.close()
            logger.info(f"closed file {self.file_path}")

