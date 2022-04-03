import sys
sys.path.append("..")

from Config.requestAPI import fetch_all
from Models.usersModel import Users
from Models.addressModel import Address
from Models.companyModel import Company

#DEFINE FUNCTION
def get_address_data(users):
    for user in users:
        user_address = user["address"]
        adresse = Address(user_address["street"],user_address["suite"],user_address["city"],user_address["zipcode"],user_address["geo"]["lat"],user_address["geo"]["lng"])
        adresse.add_address()

def get_company_data(users):
    for user in users:
        user_company = user["company"]
        company = Company(user_company["name"],user_company["catchPhrase"],user_company["bs"])
        company.add_company()


#  CALL APIs FOR USERS AND CHECK IF VALUES ISN'T None
usersFetched  = fetch_all("users")

if usersFetched == "Nice":

    get_address_data(usersFetched)
    tabAddress = Address.get_address_same()

    get_company_data(usersFetched)
    tabCompanies = Company.get_address_same()

    for user in usersFetched:

        if 'x' in user['phone']:
            phone = user['phone'].split(' ')[0]
        phone = phone.replace('.','-')

        for item in tabAddress:
            if item[1] == user["address"]["zipcode"]:
                user_address_id = item[0]

        for item in tabCompanies:
            if item[1] == user["company"]["name"]:
                user_company_id = item[0]
       
        u = Users(user['name'], user['username'], user['email'], user_address_id, phone, user['website'], user_company_id )
        u.add_users()

        
def get_Users(tab):

    if tab == "Users":
        return Users.get_all_items(tab)

    else:
        return None