"""
logger_config.py
Configures and returns a reusable logger.
"""

import logging


def configure_logger(name: str = "whisper_transcriber") -> logging.Logger:
    """
    Sets up and returns a logger instance.

    Args:
        name (str): Logger name.

    Returns:
        logging.Logger: Configured logger.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
