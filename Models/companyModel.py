import sys
sys.path.append("..")
from Config.connectDB import Database

class Address:

    def __init__(self, name = '', cphrase = '', bs = ''):
        self.name = name
        self.cphrase = cphrase
        self.bs = bs

    def add_address(self):
        print(self.name, self.cphrase, self.bs,"\n")

    @staticmethod
    def get_companies():
        print("SELECT ALL ADDRESS")
