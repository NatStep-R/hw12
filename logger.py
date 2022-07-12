import logging


def create_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel("INFO")

    file_handler = logging.FileHandler('logs/basiq.txt', encoding='utf-8')
    logger.addHandler(file_handler)
    console_handler = logging.StreamHandler()
    logger.addHandler(console_handler)

    loger_formate = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    file_handler.setFormatter(loger_formate)
    console_handler.setFormatter(loger_formate)

    return logger
