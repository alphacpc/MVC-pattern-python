import docx
from Views import postsView, commentsViews, albumView, todosView, usersView

###############DECLARATION DES VARIABLES############
doc = docx.Document("menu.docx")
listMenu = [p.text for p in doc.paragraphs]


###############DEFINITION DES FONCTIONS############
def showMenu():
    ind = 1;
    for item in listMenu:
        print(ind, ":" ,item)
        ind += 1;
    # print("\n")


###############PROGRAMME PRINCIPALE############
showMenu();
    
try :
    
    xEntre = int(input("Veuillez choisir une option : "))

    if xEntre == 1 :
        usersView.users("Users")

    elif xEntre == 2:
        postsView.posts("Posts")
        
    elif xEntre == 3:
        commentsViews.comments("Comments")

    elif xEntre == 4:
        albumView.albums("Albums")

    elif xEntre == 5:
        todosView.todos("Todos")

    elif xEntre == 6:
        print("Fermeture du programme !")

    else:
        print("A Bientot !")

except ValueError:
    print("Impossible de convertir cette chaine")
    print("A Bientot !")

