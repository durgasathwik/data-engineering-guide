import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_PATH = os.path.join(DATA_DIR, "app.log")
ERR_LOG_PATH = os.path.join(DATA_DIR, "errors.log")

age_text = "abc"
try:
    age = int(age_text)
    print(age)
except ValueError:
    print("Invalid age")

price_text = "expensive"
try:
    price = float(price_text)
    print(price)
except ValueError:
    print(f"Could not convert '{price_text}' to a price value")

logging.basicConfig(filename=LOG_PATH, level=logging.ERROR)
logging.error("Invalid row found")

logger = logging.getLogger("custom_logger")
file_handler = logging.FileHandler(ERR_LOG_PATH)
logger.addHandler(file_handler)
logger.error("This is a custom error message recorded in errors.log")
