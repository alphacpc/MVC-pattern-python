import sys
sys.path.append("..")
from Config.requestAPI import fetch_all
from Models.todosModels import Todos

todos = fetch_all("todos")


if todos != None:
    
    for todo in todos:
        
        t = Todos(todo["title"],todo["userId"],todo["completed"])
        t.add_todo()
