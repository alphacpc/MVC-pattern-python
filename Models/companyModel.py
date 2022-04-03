import sys
sys.path.append("..")
from Config.connectDB import Database

conn, cursor = Database.connexion()

class Company:

    def __init__(self, name = '', cphrase = '', bs = ''):
        self.name = name
        self.cphrase = cphrase
        self.bs = bs

    def add_company(self):
        queryInsert =  "INSERT INTO Company(name_company,catchPhrase,bs) VALUES(%s,%s,%s)"
        tup  = (self.name, self.cphrase, self.bs)
        #cursor.execute(queryInsert, tup)
        #conn.commit()



    @staticmethod
    def get_address_same():
        cursor.execute("SELECT idCompany, name_company FROM Company")
        res = cursor.fetchall()
        return res
