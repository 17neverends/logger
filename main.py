from logger import Logger
from mode import FileLogger, ConsoleLogger

if __name__ == "__main__":
    logger = Logger()

    console_logger = ConsoleLogger(format_type=2)
    logger.set_strategy(console_logger)
    logger.set_log_name("Console")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")

    file_logger = FileLogger("logfile.log", format_type=1)
    logger.set_strategy(file_logger)
    logger.set_log_name("File")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
