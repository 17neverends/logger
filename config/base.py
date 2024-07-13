from abc import ABC, abstractmethod


class LoggerStrategy(ABC):
    @abstractmethod
    def log(self, message: str, log_name: str):
        pass
