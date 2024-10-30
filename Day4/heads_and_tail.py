import random

question =  input("Head or Tail(0,1)?:.....")
radom_number = random.randint(0,1)

if int(question) == radom_number and radom_number == 1:
    print(f"You won, the answer is Head {radom_number}")
elif int(question) == radom_number and radom_number == 0:
    print(f"You won, the answer is Tail {radom_number}")

else:
    print(f"You lost, the answer is {radom_number}")