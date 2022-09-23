from faker import Faker
fake = Faker(locale="fr_Fr")

for _ in range(5):
    print(fake.numerify(text="%%%-%-%%%%-%%%%-%%%-##"))

for _ in range(5):
    print(fake.bothify(text="Product Number: ????-########"))