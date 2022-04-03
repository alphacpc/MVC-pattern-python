import sys
sys.path.append("..")

from Controllers.todosController import get_Todos;

def todos(tab):
    print("\n****LISTES DES TODOS****\n")
    print(get_Todos(tab))