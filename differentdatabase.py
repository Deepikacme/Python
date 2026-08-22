from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQL(Database):
    def connect(self):
        print("Connected to MySQL")

class MongoDB(Database):
    def connect(self):
        print("Connected to MongoDB")

databases = [MySQL(), MongoDB()]

for database in databases:
    database.connect()