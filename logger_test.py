import pytest
from logger import Logger
from mode import FileLogger, ConsoleLogger
from config.output_format import timestamp


@pytest.fixture
def console_logger(capfd):
    logger = Logger()
    console_logger = ConsoleLogger(format_type=2)
    logger.set_strategy(console_logger)
    return logger, capfd


@pytest.fixture
def file_logger(tmp_path):
    logger = Logger()
    log_file = tmp_path / "logfile.log"
    file_logger = FileLogger(log_file, format_type=1)
    logger.set_strategy(file_logger)
    return logger, log_file


def test_console_logging(console_logger):
    logger, capfd = console_logger
    logger.set_log_name("ConsoleLog")

    logger.info("1")
    logger.info("test")
    logger.info("logging")

    captured = capfd.readouterr()
    assert f"[ConsoleLog] - {timestamp} - 1" in captured.out
    assert f"[ConsoleLog] - {timestamp} - test" in captured.out
    assert f"[ConsoleLog] - {timestamp} - logging" in captured.out


def test_file_logging(file_logger):
    logger, log_file = file_logger
    logger.set_log_name("FileLog")

    logger.info("1")
    logger.info("test")
    logger.info("logging")

    with open(log_file) as f:
        log_contents = f.read()

    assert f"[FileLog] - INFO - {timestamp} - 1" in log_contents
    assert f"[FileLog] - INFO - {timestamp} - test" in log_contents
    assert f"[FileLog] - INFO - {timestamp} - logging" in log_contents


def test_output_format_console(console_logger):
    logger, capfd = console_logger
    logger.set_log_name("ConsoleLog")

    logger.info("1")

    captured = capfd.readouterr()
    output = captured.out
    count = len(output.split(" - "))
    assert count == 3


if __name__ == "__main__":
    pytest.main()
