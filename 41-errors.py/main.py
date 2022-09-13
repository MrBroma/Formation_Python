""" Exception

LBYL:
Look Before You Leap = Regarder avant de sauter

EAFP:
it's Easier to for Forgiveness than Permission
= Il est plus facile de demander pardon que de demander la permission

"""

# LBYL

from pydoc import TextRepr
from typing import Text


if "cle" in dict:
    print(dict["cle"])


# EAFP

try:
    print(dict["cle"])
except:
    pass

# ex LBYL
liste = [2, 7, "texte", 4]
total = sum(liste)

liste = [2, 7, "texte", 4]
for i in liste:
    if not str(i).isdigit():
        liste.remove(i)
total = sum(liste)

# EAFP 
liste = [2, 7, "texte", 4]
try:
    total = sum(liste)
except:
    total = 0

# ------------------------------------------------
# Gérer les exceptions

a = 5
b = 10

print(a / b)

a = 5
b = 0

try:
    resultat = a / b
except ZeroDivisionError:
    print("Division par zero impossible")
except TypeError:
    print("La variable b n'est pas du bon type")
except NameError as e:
    print("Erreur: ", e)
else:
    print("Le résultat de la division est : ", resultat)
finally:
    print("Fin du programme.")

