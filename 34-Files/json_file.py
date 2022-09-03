import json

chemin = "/home/loic/Documents/Courses/Formation_Python/34-Files/file.json"

# with open(chemin, "w") as f:
#     json.dump(list(range(10)), f, indent=4)

with open(chemin, "r") as f:
    list = json.load(f)
    print(type(list))