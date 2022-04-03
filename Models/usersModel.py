import sys
sys.path.append("..")
from Config.connectDB import Database
from Models.sameQueriesModel import BasicQuery

conn, cursor = Database.connexion()

class Users(BasicQuery):

    def __init__(self, name = '', username = '', email = '', address = '', phone = '', website = '', company = ''):
        self.name = name
        self.username = username
        self.email = email
        self.address = address
        self.phone = phone
        self.website = website
        self.company = company


    def add_users(self):
        queryInsert =  "INSERT INTO Users(name_User, username, email, idAddress_User, phone, website, idCompany_User) VALUES(%s,%s,%s,%s,%s,%s, %s)"
        tup  = (self.name, self.username, self.email, self.address, self.phone, self.website, self.company)
        cursor.execute(queryInsert, tup)
        conn.commit()