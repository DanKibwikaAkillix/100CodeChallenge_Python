print("Welcome to the rollercoaster")
height = int(input("What's your height in Cm?:>>>>> "))
age = int(input("What's your age?:>>>>> "))

# if<<height < 120 >> return <<error-message>>
#     else retrun <<cofirmation_message>>
if height>=120:
    print(" You can ride the rollercoaster!")
    if age >= 18:
        print("Enter $12")
    elif age >= 12 & age <=18:
          print("Enter $7")
    elif age <=11:
        print("Enter $5")
    else:
        print("Sorry you are not eligible")
else :
    print("Sorry, you have to grow taller before you can ride.!")