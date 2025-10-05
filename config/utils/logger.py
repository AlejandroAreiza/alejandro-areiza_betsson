from config.utils import Path, datetime, logging, sys


class ColoredFormatter(logging.Formatter):

    COLORS = {
        "DEBUG": "\033[36m",  # Cyan
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[31m",  # Red
        "CRITICAL": "\033[35m",  # Magenta
        "RESET": "\033[0m",  # Reset
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, self.COLORS["RESET"])
        reset_color = self.COLORS["RESET"]

        levelname = record.levelname
        message = record.getMessage()

        colored_levelname = f"{log_color}{levelname}{reset_color}"
        colored_message = f"{log_color}{message}{reset_color}"

        return f"{colored_levelname} - {colored_message}"


class Logger:
    _loggers = {}
    _log_file_path = None
    _initialized = False

    @classmethod
    def get_logger(cls, name: str = __name__, log_file: bool = True) -> logging.Logger:
        if name in cls._loggers:
            return cls._loggers[name]

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        logger.propagate = False

        if logger.handlers:
            return logger

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_formatter = ColoredFormatter("%(levelname)s - %(message)s")
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        # File handler - all messages with simple format
        if log_file:
            if cls._log_file_path is None:
                log_dir = Path("reports/logs")
                log_dir.mkdir(parents=True, exist_ok=True)
                cls._log_file_path = (
                    log_dir / f"test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
                )

            file_handler = logging.FileHandler(cls._log_file_path)
            file_handler.setLevel(logging.INFO)
            file_formatter = logging.Formatter(
                "%(asctime)s | %(levelname)-8s | %(message)s", datefmt="%H:%M:%S"
            )
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

        cls._loggers[name] = logger
        return logger
