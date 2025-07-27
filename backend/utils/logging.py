import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging():
    logger = logging.getLogger("my_app")
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        return logger

    os.makedirs("logs", exist_ok=True)

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
    )

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    file_handler = RotatingFileHandler("logs/app.log", maxBytes=1000000, backupCount=3)
    file_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler)

    return logger