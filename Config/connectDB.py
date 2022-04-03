import mysql.connector

class Database:

    @staticmethod
    def connexion():

        config = {
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'database': 'ApiPythonDB'
        }
        
        conn = mysql.connector.connect(**config);
        
        if conn.is_connected():
            print("Connexion avec succès !")
            cursor = conn.cursor()
            return conn, cursor

        else:
            print("Impossible de se connecter à la base de données !")
        