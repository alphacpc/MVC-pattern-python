import sys
sys.path.append("..")

from Config.requestAPI import fetch_all
from Models.usersModel import Users


#  CALL APIs FOR USERS AND CHECK IF VALUES ISN'T None
usersFetched  = fetch_all("users")

if usersFetched != None:

    for user in usersFetched:

        if 'x' in user['phone']:
            phone = user['phone'].split(' ')[0]

        phone = phone.replace('.','-')
        
        u = Users(user['name'], user['username'], user['email'], 1, phone, user['website'], 1 )
        u.insert_users()

