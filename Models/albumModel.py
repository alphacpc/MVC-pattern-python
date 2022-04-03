import sys
sys.path.append("..")
from Models.sameQueriesModel import BasicQuery
from Config.connectDB import Database

conn, cursor = Database.connexion()

class Album(BasicQuery):

    def __init__(self, title = '', userid = ''):
        self.title = title
        self.userid = userid


    def add_album(self):
        queryInsert =  "INSERT INTO Albums(title_Album, userId_Album ) VALUES(%s,%s)"
        tup  = (self.title, self.userid)
        #cursor.execute(queryInsert, tup)
        #conn.commit()
