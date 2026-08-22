from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self):
        pass


class FileLogger(Logger):
    def log(self):
        print("Logging to File")


class DatabaseLogger(Logger):
    def log(self):
        print("Logging to Database")


class ConsoleLogger(Logger):
    def log(self):
        print("Logging to Console")
loggers = [FileLogger(), DatabaseLogger(), ConsoleLogger()]
for logger in loggers:
    logger.log()