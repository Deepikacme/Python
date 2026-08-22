from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    def display_database_name(self):
        print("Database: MySQL")

class MySQL(Database):
    def connect(self):
        print("Connected to MySQL database")

obj = MySQL()
obj.connect()
obj.display_database_name()