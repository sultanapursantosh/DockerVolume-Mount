from flask import Flask
import logging

app = Flask(__name__)

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