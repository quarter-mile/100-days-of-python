import random
import my_module


random_integer = random.randint(1, 10) # includes 0 and 1 as well
print(random_integer)

print(my_module.pi)

random_float = random.random() # between 0 and 1, does not include 1
print(random_float)

random5 = random_float * 5 # number between 0.00000... and 4.99999...
print(random5)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}.")

# You can use random for flipping coins, dices, games, etc.