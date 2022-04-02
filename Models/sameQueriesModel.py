import sys
from tabulate import tabulate
sys.path.append("..")
from Config.connectDB import Database

tabNames = ["Users","Albums","Posts","Comments","Todos"]


class BasicQuery:

    @staticmethod
    def get_all_items(tabname):


        if tabname in tabNames:

            querySelect =  "SELECT * FROM " + tabname.upper()

            print(querySelect)


    @staticmethod
    def get_item_by_id(ind):

        if ind == 4:
            print("GET SINGLE ALBUM BY ID")
        
        else:
            print("ALBUM NOT FOUND !")