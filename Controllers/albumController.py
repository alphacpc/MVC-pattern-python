import sys
sys.path.append("..")
from Config.requestAPI import fetch_all
from Models.albumModel import Album

albums = fetch_all("albums")

if albums != None:
    
    for album in albums:

        p = Album(album['title'],album['userId'])
        p.add_album()


Album.get_album_by_id(4)
Album.get_album_by_id(3)
Album.get_albums()

