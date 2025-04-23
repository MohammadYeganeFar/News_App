import logging

def setup_logger(*, f_path, file_handler_level:int=10,
                  stream_handler_level:int=10,
                  frmt=None,
                  name:str):
    if frmt == None:
        frmt = "%(asctime)s:%(name)s:%(levelname)s:%(message)s"
    if name == None:
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
