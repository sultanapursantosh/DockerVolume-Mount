from flask import Flask
import logging
import os

app = Flask(__name__)
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


@app.route("/")
def home():

    logger.debug("Entered home() function")

    logger.info("Home page requested")

    logger.warning("This is a warning example")

    return "hello world"