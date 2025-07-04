import logging


def setup_logger():
    logger = logging.getLogger('app')
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger


logger = setup_logger()
