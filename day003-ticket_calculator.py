print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120 :
  print("You can ride the rollercoaster!")
  
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")

  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == ("Y" or "y"):
    bill += 3
  elif wants_photo == ("N" or "n"):
    pass
  else:
    wants_photo = input("You have entered an unaccepted value. Please answer Y for \"yes\" and N for \"no\" ")

  print(f"You final bill is ${bill}")
else:
  print("Sorry you have to grow taller before you can ride :(")