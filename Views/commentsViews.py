import sys
sys.path.append("..")

from Controllers.commentsController import get_Comments;

def comments(tab):
    print("\n****LISTES DES COMMENTAIRES****\n")
    print(get_Comments(tab))