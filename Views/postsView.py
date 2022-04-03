import sys
sys.path.append("..")

from Controllers.postsController import get_Posts;

def posts(tab):
    print("\n****LISTES DES ARTICLES****\n")
    print(get_Posts(tab))