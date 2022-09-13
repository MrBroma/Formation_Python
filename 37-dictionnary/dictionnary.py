dictionnary = {"prenom": "Paul",
"profession": "ingénieur"}


key = dictionnary.get("prenom", "La clé prénom n'existe pas")
print(key)

# Modifier la valeur associée à une clé

dictionnary["prenom"] = "Julie"

print(dictionnary)

# Ajouter ou supprimer une clé
dictionnary["age"] = 30
print(dictionnary)

if "age" in dictionnary:
  del dictionnary["age"]

# Boucler dans un dictionnaire
for x in dictionnary.values():
  print(x)

# Obtenir les clés
dictionnary.keys()
# Obtenir les valeurs
dictionnary.values()

