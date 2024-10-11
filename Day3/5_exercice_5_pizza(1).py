print("Welcome to the Python Pizza Deliveries!")
size = input("What size would you like? S, M, L : .....")
pepperoni = input("Do you want pepperoni on your Pizza? Y or N : .....")
extra_cheese = input("Do you want extra Cheese? Y or N : .....")


bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Please enter a valid size")
 

if pepperoni == "Y":
    if size == "S":
        bill +=2
    elif size == "M":
        bill +=3
    else :
        bill +=3

if extra_cheese == "Y":
    bill +=1

print(f"You bill is ${bill}")