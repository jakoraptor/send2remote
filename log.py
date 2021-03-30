#!/usr/bin/python3
"""Custom logger configuration"""
from sys import stdout
from loguru import logger as custom_logger


def formatter(log: dict) -> str:
    """
    Format log colours based on level.

    :param log: Logged event stored as map containing contextual metadata.
    :type log: dict
    :return: str
    """
    if log["level"].name == "WARNING":
        return (
            "<light-cyan>{time:DD-MM-YYYY HH:mm:ss}</light-cyan> | "
            "<light-yellow>{level}</light-yellow>: "
            "<light-white>{message}</light-white> \n"
        )
    elif log["level"].name == "ERROR":
        return (
            "<light-cyan>{time:DD-MM-YYYY HH:mm:ss}</light-cyan> | "
            "<light-red>{level}</light-red>: "
            "<light-white>{message}</light-white> \n"
        )
    else:
        return (
            "<fg #aad1f7>{time:DD-MM-YYYY HH:mm:ss}</fg #aad1f7> | "
            "<fg #67c9c4>{level}</fg #67c9c4>: "
            "<light-white>{message}</light-white> \n"
        )


def create_logger() -> custom_logger:
    """Create custom LOGGER."""
    custom_logger.remove()
    custom_logger.add(stdout, colorize=True, format=formatter)
    return custom_logger


LOGGER = create_logger()
