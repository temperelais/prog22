class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def birthday(self):
        self.age += 1
        print(self.name,"tagad ir",self.age,"gadu vecumā")

    def namechange(self,newname):
        self.name=newname
    def intro(self):
        print("Sveiki, mans dzimums ir", self.gender)
        if self.gender == "male":
            print("esmu",self.age,"gadus vecs")
        else:
            print("esmu",self.age,"gadus veca")
        print("Mani sauc",self.name)
    def genderchange(self,gender=""):
        if gender=="":
            if self.gender == "male":
                self.gender =="female"
                print("dzimums nomainīts uz female")
            else:
                self.gender =="male"
                print("dzimums nomainīts uz male")



class Woman(Human):
    def __init__(self, name, age, gender,hair_color):
        super().__init__(name, age=0, gender="female")
        self.hair_color = hair_color
        self.intro()


