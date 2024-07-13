import sys
from config.base import LoggerStrategy
from config.level import LogLevel
from config.output_format import format_type_2, formatters, timestamp


class ConsoleLogger(LoggerStrategy):
    def __init__(self, format_type: int):
        self.format_type = format_type

    def log(self, message: str, log_name: str, log_level: LogLevel):
        log_message = formatters.get(self.format_type, format_type_2)(
            log_name, log_level, timestamp, message
        )
        print(log_message, file=sys.stdout)


class FileLogger(LoggerStrategy):
    def __init__(self, filename: str, format_type: int):
        self.filename = filename
        self.format_type = format_type

    def log(self, message: str, log_name: str, log_level: LogLevel):
        log_message = formatters.get(self.format_type, format_type_2)(
            log_name, log_level, timestamp, message
        )
        with open(self.filename, 'a') as f:
            f.write(log_message)
