import logging


logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console": {
                "format": "%(asctime)s - level: %(levelname)s \
                    - message: %(message)s from: %(funcName)-8s - %(name)-8s",
                "datefmt": "%H:%M:%S",
            },
            "file": {
                "format": "%(asctime)s %(levelname)-8s - message: %(message)8s \
                    - from: %(funcName)-8s - (%(filename)-12s)",
                "datefmt": "%d-%b-%Y %H:%M:%S",
            },
        },
        "handlers": {
            "console": {"class": "logging.StreamHandler", "formatter": "console"},
            "file": {
                "level": "DEBUG",
                "class": "logging.FileHandler",
                "formatter": "file",
                "filename": "./projet_13.log",
            },
        },
        "loggers": {"": {"level": "WARNING", "handlers": ["console", "file"]}},
    }
)

logging.info("It's breadcrumbs")
logging.error("It's an event error", extra=dict(bar=43))
logging.exception("An exception happened")

logger = logging.getLogger(__name__)
