import sys
sys.path.append("..")
from Config.requestAPI import fetch_all
from Models.postsModel import Posts

posts = fetch_all("posts")

if posts != None:
    
    for post in posts:

        p = Posts(post['title'],post['body'].replace("\n"," "),post['userId'])
        p.add_posts()


def get_Posts(tab):
    
    if tab == "Posts":
        return Posts.get_all_items(tab)

    else:
        return None