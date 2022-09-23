from faker import Faker
fake = Faker(locale="fr_Fr")  # fake = Faker(locale="en_US")

# method name(), text() and address()
# print(fake.name())
# print(fake.text())
# print(fake.address())

#################################

# Generate unique data
# print(fake.unique.name())

# with number and verif if it's unique
# for _ in range (500):
#     print(fake.unique.random_int())

# numbers = [fake.unique.random_int() for _ in range(500)]
# Ne lèvera jamais de AssertionError set --> jamais la même valeur
# assert len(numbers) == len(set(numbers))


# test avec erreur
# numbers2 = [1, 2, 2]
# assert len(numbers2) == len(set(numbers2))

# for _ in range(1000):
#     print(fake.unique.first_name())
#
# for _ in range(1000):
#     print(fake.unique.text())

# for _ in range(10):
#     print(fake.job())
#
# for _ in range(10):
#     print(fake.file_path())
#
# for _ in range(10):
#     print(fake.file_path(depth=5, category='video'))

for _ in range(10):
    print(fake.credit_card_number(), fake.credit_card_expire(), fake.credit_card_security_code())

for _ in range(10):
    print(fake.rgb_color())
    print(fake.hex_color())


