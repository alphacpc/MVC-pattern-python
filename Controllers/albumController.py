import sys
sys.path.append("..")
from Config.requestAPI import fetch_all
from Models.albumModel import Album

albums = fetch_all("albums")

if albums != None:
    
    for album in albums:

        a = Album(album['title'],album['userId'])
        a.add_album()


def get_Albums(tab):
    
    if tab == "Albums":
        return Album.get_all_items(tab)

    else:
        return None