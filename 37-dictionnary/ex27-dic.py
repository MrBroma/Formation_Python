films = {"Le seigneur des Anneaux": 12,
         "Harry Potter": 9,
         "Blade Runner": 7.5
        }

prix = 0

for i in films.values():
    prix += i

print(prix)

# exercie 28
employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }
            
del employes["id03"]
employes["id02"]["age"] = 26
age_paul = employes["id01"]["age"]
print(age_paul)