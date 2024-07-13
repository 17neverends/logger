from config.base import LoggerStrategy
from config.level import LogLevel


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.strategy = None
            cls._instance.log_name = "Logger"
        return cls._instance

    def set_strategy(self, strategy: LoggerStrategy):
        self.strategy = strategy

    def set_log_name(self, log_name: str):
        self.log_name = log_name

    def log(self, message: str, log_level: LogLevel):
        if self.strategy:
            self.strategy.log(message, self.log_name, log_level)
        else:
            raise ValueError("Logging strategy not set")

    def info(self, message: str):
        self.log(message, LogLevel.INFO)

    def warning(self, message: str):
        self.log(message, LogLevel.WARNING)

    def error(self, message: str):
        self.log(message, LogLevel.ERROR)

    def debug(self, message: str):
        self.log(message, LogLevel.DEBUG)
