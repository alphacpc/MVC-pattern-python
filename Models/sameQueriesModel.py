import sys
sys.path.append("..")
from Config.connectDB import Database

class BasicQuery:

    @staticmethod
    def get_all_items():
        print("SELECT ALL ALBUMS")


    @staticmethod
    def get_item_by_id(ind):

        if ind == 4:
            print("GET SINGLE ALBUM BY ID")
        
        else:
            print("ALBUM NOT FOUND !")