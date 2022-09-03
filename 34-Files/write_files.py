# mode write which overwrite in the file
chemin  = "/home/loic/Documents/Courses/Formation_Python/34-Files/fichier.txt"

with open(chemin, "w") as f:
    f.write("Bonjour")

# mode a for append
chemin  = "/home/loic/Documents/Courses/Formation_Python/34-Files/fichier.txt"

with open(chemin, "a") as f:
    f.write("Bonjour")

# mode a for append on antoher line with /n
chemin  = "/home/loic/Documents/Courses/Formation_Python/34-Files/fichier.txt"

with open(chemin, "a") as f:
    f.write("\nBonjour")