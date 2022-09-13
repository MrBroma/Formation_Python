d = {"prenom": "Paul",
"profession": "ingénieur"}


key = d.get("prenom", "La clé prénom n'existe pas")
print(key)

# Modifier la valeur associée à une clé

d["prenom"] = "Julie"

print(d)

# Ajouter ou supprimer une clé
d["age"] = 30
print(d)

if "age" in d:
  del d["age"]

# Boucler dans un dictionnaire
for x in d.values():
  print(x)

# Obtenir les clés
d.keys()
# Obtenir les valeurs
d.values()

