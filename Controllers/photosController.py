import sys
sys.path.append("..")
from Config.requestAPI import fetch_all
from Models.photosModel import Photos

photos = fetch_all("photos")

if photos != None:
    
    for photo in photos:

        ph = Photos(photo['title'], photo['url'], photo['thumbnailUrl'], photo['albumId'])
        ph.add_photos()


