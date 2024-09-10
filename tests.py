class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def birthday(self):
        self.age += 1

        

person = Human("sdjsdjiw",3,"male")

print(person.name)
print(person.gender)
print(person.age)

person.birthday()

print(person.age)

print("Sveiki, mans dzimums ir", person.gender)
if person.gender == "male":
    print("esmu",person.age,"gadus vecs")
else:
    print("esmu",person.age,"gadus veca")
print("Mani sauc",person.name)


