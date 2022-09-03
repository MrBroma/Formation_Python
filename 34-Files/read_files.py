chemin  = "/home/loic/Documents/Courses/Formation_Python/34-Files/fichier.txt"

# f = open(chemin, "r")
# f.close()
# print(f)

# only use this method with open
with open(chemin, "r") as f:
    contenu = f.read()
    print(contenu)

# with the /n symbole
with open(chemin, "r") as f:
    contenu = repr(f.read())
    print(contenu)

# strings in list but with the /n
with open(chemin, "r") as f:
    contenu = f.readlines()
    print(contenu)

# strings in list without the /n
with open(chemin, "r") as f:
    contenu = f.read().splitlines()
    print(contenu)

