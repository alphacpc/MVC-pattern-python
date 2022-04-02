import sys
sys.path.append("..")
from Config.requestAPI import fetch_all
from Models.postsModel import Posts

posts = fetch_all("posts")

if posts != None:
    
    for post in posts:

        p = Posts(post['title'],post['body'],post['userId'])
        p.add_posts()


Posts.get_post_by_id(4)
Posts.get_post_by_id(3)
Posts.get_posts()
