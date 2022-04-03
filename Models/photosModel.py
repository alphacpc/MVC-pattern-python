import sys
sys.path.append("..")
from Config.connectDB import Database
from Models.sameQueriesModel import BasicQuery

conn, cursor = Database.connexion()

class Photos(BasicQuery):

    def __init__(self, title = '', url = '', thumbnail = '', albumId = ''):
        self.title = title
        self.url = url
        self.thumbnail = thumbnail
        self.albumId = albumId


    def add_photos(self):
        queryInsert =  "INSERT INTO Photos(title_Photo, url_Photo, thumbnailUrl, albumId  ) VALUES(%s, %s, %s, %s)"
        tup  = (self.title, self.url, self.thumbnail, self.albumId)
        # print(tup)
        # cursor.execute(queryInsert, tup)
        # conn.commit()
