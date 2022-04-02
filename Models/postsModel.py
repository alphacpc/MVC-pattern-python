import sys
sys.path.append("..")
from Config.connectDB import Database
from Models.sameQueriesModel import BasicQuery

class Posts(BasicQuery):

    def __init__(self, title = '', body = '', userid = ''):
        self.title = title
        self.body = body
        self.userid = userid


    def add_posts(self):
        print(self.title, self.body, self.userid,"\n")
