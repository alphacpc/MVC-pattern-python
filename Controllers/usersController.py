import sys
sys.path.append("..")

from Config.requestAPI import fetch_all
from Models.usersModel import Users
from Models.addressModel import Address

#DEFINE FUNCTION
def get_address_data(users):
    for user in users:
        user_address = user["address"]
        adresse = Address(user_address["street"],user_address["suite"],user_address["city"],user_address["zipcode"],user_address["geo"]["lat"],user_address["geo"]["lng"])
        adresse.add_address()

def get_company_data(users):
    for user in users:
        user_address = user["address"]
        adresse = Address(user_address["street"],user_address["suite"],user_address["city"],user_address["zipcode"],user_address["geo"]["lat"],user_address["geo"]["lng"])
        adresse.add_address()


#  CALL APIs FOR USERS AND CHECK IF VALUES ISN'T None
usersFetched  = fetch_all("users")

if usersFetched != None:

    get_address_data(usersFetched)
    
    tabAddress = Address.get_address_same()

    for user in usersFetched:

        if 'x' in user['phone']:
            phone = user['phone'].split(' ')[0]

        phone = phone.replace('.','-')

        for item in tabAddress:

            if item[1] == user["address"]["zipcode"]:
                user_address = item[0]
        
        # u = Users(user['name'], user['username'], user['email'], user_address, phone, user['website'], 1 )
        

        # adresse = Address()
        # print(u.email)
        

# Users.get_all_items("Users")