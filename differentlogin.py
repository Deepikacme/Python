from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def login(self):
        pass

class PasswordLogin(Authentication):
    def login(self):
        print("Login using Password")

class GoogleLogin(Authentication):
    def login(self):
        print("Login using Google")

methods = [PasswordLogin(), GoogleLogin()]

for method in methods:
    method.login()