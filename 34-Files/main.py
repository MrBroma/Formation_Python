import json

with open("data.json", "r") as f:
    data = json.load(f)

data.append(4)

with open("data.json", "w") as f:
    data = json.dump(data, f, indent=4)

# if we use f.read()
# use f.seek(0) to return at the start

# error
# Pèche
# in python file --> json.dump("Pèche", f, ensure_ascii=False)
