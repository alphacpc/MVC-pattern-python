import sys
sys.path.append("..")
from Config.requestAPI import fetch_all
from Models.albumModel import Album

albums = fetch_all("albums")

if albums != None:
    
    for album in albums:

        p = Album(album['title'],album['userId'])
        # p.add_album()


Album.get_all_items("Albums")