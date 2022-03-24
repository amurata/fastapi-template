import os

import toml
import yaml
from logging import getLogger
from logging.config import dictConfig


def init_logger(filepath: str):
    # config_path = "logging_conf2.yaml"
    with open(filepath) as f:
        config = yaml.safe_load(f)
        # print(config)
        dictConfig(config)
        
        
def init_gunicorn_uvicorn_logger(filepath: str):
    import logging
    from fastapi.logger import logger as fastapi_logger

    if "gunicorn" in os.environ.get("SERVER_SOFTWARE", ""):
        '''
        gunicornで起動した場合のみ、loggerを切り替える必要がある
        '''  
        init_logger(filepath)
        gunicorn_logger = logging.getLogger("gunicorn")
        log_level = gunicorn_logger.level

        root_logger = logging.getLogger()
        gunicorn_error_logger = logging.getLogger("gunicorn.error")
        uvicorn_access_logger = logging.getLogger("uvicorn.access")

        # Use gunicorn error handlers for root, uvicorn, and fastapi loggers
        root_logger.handlers = gunicorn_error_logger.handlers
        uvicorn_access_logger.handlers = gunicorn_error_logger.handlers
        fastapi_logger.handlers = gunicorn_error_logger.handlers

        # Pass on logging levels for root, uvicorn, and fastapi loggers
        root_logger.setLevel(log_level)
        uvicorn_access_logger.setLevel(log_level)
        fastapi_logger.setLevel(log_level)



def get_logger(name: str):
    return getLogger(name)