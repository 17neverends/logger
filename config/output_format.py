from datetime import datetime


def format_type_1(log_name: str, log_level: str, timestamp: str, message: str):
    return f"[{log_name}] - {log_level.value} - {timestamp} - {message}\n"


def format_type_2(log_name: str, _, timestamp: str, message: str):
    return f"[{log_name}] - {timestamp} - {message}\n"


formatters = {
                1: format_type_1,
                2: format_type_2
             }

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
