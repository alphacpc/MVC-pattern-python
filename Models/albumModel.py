import sys
sys.path.append("..")
from Config.connectDB import Database

class Album:

    def __init__(self, title = '', userid = ''):
        self.title = title
        self.userid = userid


    def add_album(self):
        print(self.title, self.userid,"\n")

    @staticmethod
    def get_albums():
        print("SELECT ALL ALBUMS")


    @staticmethod
    def get_album_by_id(ind):

        if ind == 4:
            print("GET SINGLE ALBUM BY ID")
        
        else:
            print("ALBUM NOT FOUND !")