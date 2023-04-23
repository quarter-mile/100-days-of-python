age = input("What is your current age? ")

int_age = int(age)
left = 90 - int_age

days = left * 365
weeks = left * 52
months = left * 12

print(f"You have {days} days, {weeks} weeks, or {months} months left.")
