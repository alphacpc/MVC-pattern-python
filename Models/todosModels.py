import sys
sys.path.append("..")
from Config.connectDB import Database
from Models.sameQueriesModel import BasicQuery

class Todos(BasicQuery):

    def __init__(self, title = '', userid = ''):
        self.title = title
        self.userid = userid


    def add_todo(self):
        print(self.title, self.userid,"\n")

