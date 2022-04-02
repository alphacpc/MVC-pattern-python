import sys
sys.path.append("..")
from Config.connectDB import Database

class Comments:

    def __init__(self, name = '', email = '', body = '', postid = ''):
        self.name = name
        self.email = email
        self.body = body
        self.postid = postid


    def add_comments(self):
        print(self.name, self.email, self.body, self.postid,"\n")

    @staticmethod
    def get_comments():
        print("SELECT ALL COMMENTS")


    @staticmethod
    def get_comment_by_id(ind):

        if ind == 4:
            print("GET SINGLE COMMENT BY ID")
        
        else:
            print("COMMENT NOT FOUND !")