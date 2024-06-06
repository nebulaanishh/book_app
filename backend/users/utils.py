import logging

logger = logging.getLogger(__name__)
logger_debug = logging.basicConfig(
    filename="backend-log.log", filemode="a", encoding="utf-8", level=logging.DEBUG
)
logger_error = logging.basicConfig(
    filename="backend-log.log", filemode="a", encoding="utf-8", level=logging.ERROR
)
logger_info = logging.basicConfig(
    filename="backend-log.log", filemode="a", encoding="utf-8", level=logging.INFO
)
