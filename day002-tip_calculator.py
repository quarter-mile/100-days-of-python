bill = input("Welcome to the tip calculator.\nWhat was the total bill? $")
bill = float(bill)

tip = input("What percentage of tip would you like to give? 10, 12, or 15? ")
tip = 1 + (int(tip) / 100)

people = input("How many people to split the bill? ")
people = int(people)

part = round(bill / people * tip, 2)

print(f"Each person should pay: ${part}")