import sys
sys.path.append("..")
from Config.connectDB import Database

class Users:

    def __init__(self, name = '', username = '', email = '', address = '', phone = '', website = '', company = ''):
        self.name = name
        self.username = username
        self.email = email
        self.address = address
        self.phone = phone
        self.website = website
        self.company = company


    def insert_users(self):
        print(self.name, self.username, self.email, self.address, self.phone, self.website, self.company)

    @staticmethod
    def get_users():
        print("Select All USERS")


    @staticmethod
    def get_user_by_id(ind):

        if ind == 4:
            print("Select user Alpha")
        
        else:
            print("User not found !")

    @staticmethod
    def update_user():
        print("Updated user")
    