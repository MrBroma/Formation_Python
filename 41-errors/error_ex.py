fichier = input("Entrez un fichier à ouvrir : ")

try:
    f = open(fichier, "r")
    print(f.read())
except FileNotFoundError:
    print("Le fichier n'existe pas")
except UnicodeDecodeError:
    print("Impossible de lire le fichier")
else:
    f.close()


