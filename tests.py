class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def birthday(self):
        self.age += 1

    def namechange(self,newname):
        self.name=newname
    def intro(self):
        print("Sveiki, mans dzimums ir", self.gender)
        if self.gender == "male":
            print("esmu",self.age,"gadus vecs")
        else:
            print("esmu",self.age,"gadus veca")
        print("Mani sauc",self.name)
    def genderchange(self,newg):
        self.gender=newg

person = Human("sdjsdjiw",3,"male")

print(person.name)
print(person.gender)
print(person.age)

person.birthday()

print(person.age)

person.namechange("yeajkls")


