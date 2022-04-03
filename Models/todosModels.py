import sys
sys.path.append("..")
from Config.connectDB import Database
from Models.sameQueriesModel import BasicQuery

conn, cursor = Database.connexion()

class Todos(BasicQuery):

    def __init__(self, title = '', userid = '', status = ''):
        self.title = title
        self.userid = userid
        self.status = status


    def add_todo(self):
        queryInsert =  "INSERT INTO Todos(title_Todo, userId_Todo, status) VALUES(%s,%s,%s)"
        tup  = (self.title, self.userid, self.status)
        # cursor.execute(queryInsert, tup)
        # conn.commit()
