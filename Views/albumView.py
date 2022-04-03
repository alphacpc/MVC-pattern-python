import sys
sys.path.append("..")

from Controllers.albumController import get_Albums;

def albums(tab):
    print("\n****LISTES DES ALBUMS****\n")
    print(get_Albums(tab))