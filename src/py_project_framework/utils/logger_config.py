import logging


def get_logger(logger_name, log_level=logging.INFO):
    # Create logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    log_file = 'tests/logs/application.log'

    # Create handlers
    s_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(log_file)
    s_handler.setLevel(log_level)
    f_handler.setLevel(log_level)

    # Create formatters and add it to handlers
    log_format = "%(asctime)s-%(filename)s-%(lineno)d-%(levelname)s-%(message)s"
    formatter = logging.Formatter(log_format, datefmt="%Y-%m-%d %H:%M")
    s_handler.setFormatter(formatter)
    f_handler.setFormatter(formatter)

    logger.addHandler(s_handler)
    logger.addHandler(f_handler)

    return logger


if __name__ == '__main__':
    log = get_logger('sample.py')
    log.info('sample info message')
