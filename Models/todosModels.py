import sys
sys.path.append("..")
from Config.connectDB import Database

class Todos:

    def __init__(self, title = '', userid = ''):
        self.title = title
        self.userid = userid


    def add_todo(self):
        print(self.title, self.userid,"\n")

    @staticmethod
    def get_todos():
        print("SELECT ALL TODOS")


    @staticmethod
    def get_todo_by_id(ind):

        if ind == 4:
            print("GET SINGLE TODO BY ID")
        
        else:
            print("TODO NOT FOUND !")