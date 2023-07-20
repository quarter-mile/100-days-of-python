import random


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
length = len(names)
whois = random.randint(0, length-1)
print(names[whois] + " is going to buy the meal today!")
