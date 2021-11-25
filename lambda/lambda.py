import logging
import os, sys

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def handler(event, context):
    LOGGER.info("I've been called!")
    return {
        "message": "Hello pytest!"
    }