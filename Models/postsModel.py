import sys
sys.path.append("..")
from Config.connectDB import Database
from Models.sameQueriesModel import BasicQuery

conn, cursor = Database.connexion()

class Posts(BasicQuery):

    def __init__(self, title = '', body = '', userid = ''):
        self.title = title
        self.body = body
        self.userid = userid


    def add_posts(self):
        queryInsert =  "INSERT INTO Posts(title_Post, body_Post, userId_Post ) VALUES(%s,%s,%s)"
        tup  = (self.title, self.body, self.userid)
        # cursor.execute(queryInsert, tup)
        # conn.commit()