import sys
sys.path.append("..")
from Config.connectDB import Database

conn, cursor = Database.connexion()

class Address:

    def __init__(self, street = '', suite = '', city = '', zipcode = '', lat = '', lng = ''):
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.lat = lat
        self.lng = lng


    def add_address(self):

        queryInsert =  "INSERT INTO Address(street, suite, city, zipcode, lat, lng) VALUES(%s,%s,%s,%s,%s,%s)"
        tup  = (self.street, self.suite, self.city, self.zipcode, self.lat, self.lng)
        # print(tup)
        # cursor.execute(queryInsert, tup)
        # conn.commit()


    @staticmethod
    def get_address_same():
        cursor.execute("SELECT idAddress, zipcode FROM Address")
        res = cursor.fetchall()
        return res