import sys
from fastapi import FastAPI

# Configure logs
import logging
from fastapi.logger import logger as fastapi_logger
gunicorn_error_logger = logging.getLogger("gunicorn.error")
gunicorn_logger = logging.getLogger("gunicorn")
uvicorn_access_logger = logging.getLogger("uvicorn.access")
uvicorn_access_logger.handlers = gunicorn_error_logger.handlers

fastapi_logger.handlers = gunicorn_error_logger.handlers

if __name__ != "__main__":
    fastapi_logger.setLevel(gunicorn_logger.level)
else:
    fastapi_logger.setLevel(logging.DEBUG)

app = FastAPI()

@app.get("/")
async def func_home():
    logger = logging.getLogger("gunicorn.error")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.error("loglevel="+logging.getLevelName(logger.getEffectiveLevel()))
    return {"message": "index"}

@app.get("/ping")
async def func_ping():
    fastapi_logger.info("info")
    fastapi_logger.error("error")
    return {"message": "pong"}
