from abc import ABC, abstractmethod

class CloudStorage(ABC):
    @abstractmethod
    def storage(self):
        pass


class GoogleDrive(CloudStorage):
    def storage(self):
        print("Using Google Drive")


class AWSStorage(CloudStorage):
    def storage(self):
        print("Using AWS Storage")


class AzureStorage(CloudStorage):
    def storage(self):
        print("Using Azure Storage")
storages = [GoogleDrive(), AWSStorage(), AzureStorage()]
for storage in storages:
    storage.storage()