import os

def function_name():
    print("I am a function")

function_name()

# return a value (end of the function)

def return_five():
    return 5
    print("fin de la fonction") # code innategnable

a = return_five()
print(a)

def verif_file():
    if os.path.exists("fichier.txt"):
        return True
    else:
        return False

# plus simplement
def verif_file2():
    if os.path.exists("fichier.txt"):
        return True
    return False

def verif_file3():
    return os.path.exists("fichier.txt")

# Par défaut une fonction retourne None
def test():
    pass

a = test()
print(a)

# arguments
def affiche(message): # paramètre
    print(message)

affiche("bonjour") # argument

# Ne pas afficher d'erreur
def affiche(message="Message par défaut"): # paramètre
    print(message)

affiche()

def addition(a, b):
    return a + b

addition(5, 10)
# ou
addition(b=10, a=5)

