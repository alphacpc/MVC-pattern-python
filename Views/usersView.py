import sys
sys.path.append("..")

from Controllers.usersController import get_Users;

def users(tab):
    print("\n****LISTES DES UTILISATEURS****\n")
    print(get_Users(tab))