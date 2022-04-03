import queue
import sys
from tabulate import tabulate
sys.path.append("..")
from Config.connectDB import Database

conn, cursor = Database.connexion()

list_Header_Query = [
    {"table" : "Users", "head" : ["name_User","username", "email", "phone", "website"], "query" : "SELECT name_User, username, email, phone, website FROM "},
    {"table" : "Todos", "head" : ["title_Todo","author_id"], "query" : "SELECT title_Todo, userId_Todo FROM " },
    {"table" : "Albums", "head" : ["title_Album","user_Name", "user_Email"], "query" : "SELECT title_Album, userId_Album FROM "},
    {"table" : "Posts", "head" : ["title_Post","author_id"], "query" : "SELECT title_Post, userId_Post FROM "},
    {"table" : "Comments", "head" : ["name_Comment","email_Comment_author"], "query" : "SELECT name_Comment, email_Comment FROM " },
]

class BasicQuery:

    @staticmethod
    def get_all_items(tabname):

        for child in list_Header_Query:
            if child['table'] == tabname:
                head = child['head']
                query = child['query']

        cursor.execute(query  + tabname)

        result = cursor.fetchall()

        return tabulate(result, headers = head, tablefmt = 'psql')


    #APPORTER DES AMELIORATIONS
    @staticmethod
    def get_item_by_id(ind):
        pass