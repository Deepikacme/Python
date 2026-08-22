from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

class PasswordAuth(Authentication):
    def login(self):
        print("Login using Password")

    def logout(self):
        print("Logged out from Password Account")

class OTPAuth(Authentication):
    def login(self):
        print("Login using OTP")

    def logout(self):
        print("Logged out from OTP Account")

p = PasswordAuth()
o = OTPAuth()

p.login()
p.logout()

o.login()
o.logout()