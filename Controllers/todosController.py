import sys
sys.path.append("..")
from Config.requestAPI import fetch_all
from Models.todosModels import Todos

todos = fetch_all("todos")

if todos != None:
    
    for todo in todos:

        p = Todos(todo['title'],todo['userId'])
        p.add_todo()


Todos.get_todo_by_id(4)
Todos.get_todo_by_id(3)
Todos.get_todos()

