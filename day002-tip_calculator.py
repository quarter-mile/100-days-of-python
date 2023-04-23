bill = float(input("Welcome to the tip calculator.\nWhat was the total bill? $"))

tip = 1 + (int(input("What percentage of tip would you like to give? 10, 12, or 15? ")) / 100)

people = int(input("How many people to split the bill? "))

part = round(bill / people * tip, 2)

print(f"Each person should pay: ${part}")
