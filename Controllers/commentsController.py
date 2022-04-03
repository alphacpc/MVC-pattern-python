import sys
sys.path.append("..")
from Config.requestAPI import fetch_all
from Models.commentsModels import Comments

comments = fetch_all("comments")

if comments != None:
    
    for comment in comments:

        c = Comments(comment['name'], comment['email'], comment['body'].replace("\n"," "), comment['postId'])
        c.add_comments()


