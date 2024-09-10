class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

person = Human("Janis",3,"male")

print(person.name)
print(person.gender)
print(person.age)