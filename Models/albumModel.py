import sys
sys.path.append("..")
from Models.sameQueriesModel import BasicQuery
from Config.connectDB import Database

class Album(BasicQuery):

    def __init__(self, title = '', userid = ''):
        self.title = title
        self.userid = userid


    def add_album(self):
        print(self.title, self.userid,"\n")

