import logging
import logging.config

from colorama import init

init()


LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {"standard": {"format": "%(message)s"}},
    "handlers": {
        "default": {
            "level": "DEBUG",
            "formatter": "standard",
            "class": "logging.StreamHandler",
        }
    },
    "loggers": {
        "docker_registry_cli": {
            "handlers": ["default"],
            "level": "INFO",
            "propagate": True,
        }
    },
}

logging.config.dictConfig(LOGGING)
