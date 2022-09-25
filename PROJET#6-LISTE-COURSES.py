# variable choix
choix = "None"
# Création de la liste de course vide (départ)
liste = []

while choix != "5":
    # Demander à l'utilisateur l'action a réaliser sur la liste de course
    choix = input("""
__________________________________________________
Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste de courses
2: Retirer un élément de la liste de courses
3: Afficher les éléments de la liste de courses
4: Vider la liste de courses
5: Quitter le programme
Votre choix : """)
    if not choix.isdigit():
        print("Veuillez choisir une question de 1 à 5 !")

    if choix.isdigit():
        choix = int(choix)
        if choix < 1 or choix > 5:
            print("Veuillez choisir une question de 1 à 5 !")
            continue

    # condition en fonction du choix de l'utilisateur
    if choix == 1:
        choix1 = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        if choix1 in liste:
            print(f"L'élément {choix1} existe déjà dans la liste.")
        else:
            liste.append(choix1)
            print(f"L'élément {choix1} a été ajouté à la liste.")

    elif choix == 2:
        choix2 = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if choix2 in liste:
            liste.remove(choix2)
            print(f"L'élément {choix2} a été supprimé de la liste.")

        else:
            print(f"L'élément {choix2} n'est pas dans la liste.")

    elif choix == 3:
        if liste == []:
            print("La liste est vide")
        else:
            print("Voici le contenu de votre liste : ")
            for i in liste:
                print(f"{liste.index(i) + 1}. {i}\n")

    elif choix == 4:
        if liste == []:
            print("La liste est déjà vide!!")
        else:
            liste = []
            print("La liste a été vidée de son contenu")
    else:
        choix = str(choix)

print("A bientôt !")