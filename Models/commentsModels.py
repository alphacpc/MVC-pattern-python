import sys
sys.path.append("..")
from Config.connectDB import Database
from Models.sameQueriesModel import BasicQuery

conn, cursor = Database.connexion()

class Comments(BasicQuery):

    def __init__(self, name = '', email = '', body = '', postid = ''):
        self.name = name
        self.email = email
        self.body = body
        self.postid = postid


    def add_comments(self):
        # A executer qu'une seule fois
        queryInsert =  "INSERT INTO Comments(name_Comment, email_Comment, body_Comment, postId ) VALUES(%s,%s, %s, %s)"
        tup  = (self.name, self.email, self.body, self.postid)
        cursor.execute(queryInsert, tup)
        conn.commit()
