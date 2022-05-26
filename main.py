import json
from faker import Faker
fake_ru = Faker("ru_RU")

dict = {}

for i in range(1,251):
    name = fake_ru.name()
    tn = fake_ru.phone_number()
    j = fake_ru.job()
    A = fake_ru.address()
    dict[i] = {name: [A, j, tn]}
    with open ("DS.txt", 'w', encoding= 'utf-8') as f:
        json.dump(dict, f, indent=4, ensure_ascii= False)
    # print(fake_ru.name())
    # print(fake_ru.phone_number())
    # print(fake_ru.job())
    # print(fake_ru.address())


