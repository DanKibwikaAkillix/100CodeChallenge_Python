print("Welcome to the rollercoaster")
height = int(input("What's your height in Cm?:>>>>> "))
age = int(input("What's your age?:>>>>> "))

bill = 0
# if<<height < 120 >> return <<error-message>>
#     else retrun <<cofirmation_message>>
if height>=120:
    print(" You can ride the rollercoaster!")
    if age >= 18:
        bill = 12
        print(f"You will pay ${bill}")

    elif age >= 12 & age <=18:
          bill = 7
          print(f"You will pay ${bill}")

    elif age <12:
        bill = 5
        print(f"You will pay ${bill}")

    photo = input("Do you want a photo taken? Y or N. ")

    if photo == "Y":
            bill +=3
            print(f"You will add $3 variable now you will be paying {bill}")

    else:
            print(f"Your amount is ${bill}")

            
  
else :
    print("Sorry, you have to grow taller before you can ride.!")