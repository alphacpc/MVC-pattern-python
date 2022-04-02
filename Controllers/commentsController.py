import sys
sys.path.append("..")
from Config.requestAPI import fetch_all
from Models.commentsModels import Comments

comments = fetch_all("comments")

if comments != None:
    
    for comment in comments:

        p = Comments(comment['name'], comment['email'], comment['body'], comment['postId'])
        # p.add_comments()


Comments.get_all_items("Comments")
