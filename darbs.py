from tests import Human, Woman

human_list = []

for i in range(20):
    human_list.append(Human("Hugo",i,"male"))

for Human in human_list:
    if Human.age % 2 == 0:
        Human.genderchange()
    Human.intro()