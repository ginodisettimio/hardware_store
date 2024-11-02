import os
import logging
from logging.handlers import TimedRotatingFileHandler


def config_logger(debug_level: bool) -> None:
    LOGS_PATH = './logs'
    if not os.path.exists(LOGS_PATH):
        os.makedirs(name=LOGS_PATH)

    log_filename = LOGS_PATH + '/hardware.log'
    logger = logging.getLogger()
    logger.setLevel(level=logging.DEBUG if debug_level else logging.INFO)

    handler = TimedRotatingFileHandler(
        filename=log_filename,
        when='midnight',
        interval=1,
        backupCount=0,
    )
    handler.suffix = '%Y%m%d'
    logger.addHandler(handler)

    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    handler.setFormatter(formatter)
