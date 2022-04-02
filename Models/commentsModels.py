import sys
sys.path.append("..")
from Config.connectDB import Database
from Models.sameQueriesModel import BasicQuery

class Comments(BasicQuery):

    def __init__(self, name = '', email = '', body = '', postid = ''):
        self.name = name
        self.email = email
        self.body = body
        self.postid = postid


    def add_comments(self):
        print(self.name, self.email, self.body, self.postid,"\n")

