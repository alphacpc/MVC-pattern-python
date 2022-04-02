import sys
sys.path.append("..")
from Config.connectDB import Database

class Posts:

    def __init__(self, title = '', body = '', userid = ''):
        self.title = title
        self.body = body
        self.userid = userid


    def add_posts(self):
        print(self.title, self.body, self.userid,"\n")

    @staticmethod
    def get_posts():
        print("SELECT ALL POSTS")


    @staticmethod
    def get_post_by_id(ind):

        if ind == 4:
            print("GET SINGLE POST BY ID")
        
        else:
            print("POST NOT FOUND !")
