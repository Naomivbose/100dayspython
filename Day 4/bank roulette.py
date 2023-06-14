import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
number_names = len(names)
random_number = random.randint(0, number_names - 1)
person_who_pays = names[random_number]
print (person_who_pays + " is going to buy the meal today!")
