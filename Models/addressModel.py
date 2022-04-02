import sys
sys.path.append("..")
from Config.connectDB import Database

class Address:

    def __init__(self, street = '', suite = '', city = '', zipcode = '', lat = '', lng = ''):
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.lat = lat
        self.lng = lng


    def add_address(self):
        print(self.street, self.suite, self.city, self.zipcode, self.lat, self.lng,"\n")

    @staticmethod
    def get_address():
        print("SELECT ALL ADDRESS")
