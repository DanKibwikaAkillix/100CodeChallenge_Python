import random


rock = ''' 

   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''

    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
 '''

sizor = '''
  _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

 '''

nameList = [rock, paper, sizor]
question = int(input("let play: Rock[1] , Paper[2], Sizor[3]:?...."))

i = question-1 #for indexing
userResponse = nameList[i]

computeranswer = random.randint(0,2)
computerResponse = nameList[computeranswer]

if int(i) == computeranswer :
    print(f"Play again")
    print(f"""You:{userResponse}""")
    print(f"""Computer: {computerResponse}""")

#Assuming  R = Rock[0], P = Paper[1], S= Sizor[2]

# if R[0] against P[1], P wins
elif int(i) == 0 and computeranswer == 1:
    print("Computer Won, Paper swollows the Rock")
    print(f"""You:{userResponse}""")
    print(f"""Computer: {computerResponse}""")

# if R[0] against S[2] , R WINS
elif int(i) == 0 and computeranswer == 2:
    print("You Won, Rock breaks the Sizor")
    print(f"""You:{userResponse}""")
    print(f"""Computer: {computerResponse}""")

# if P[1] against S[2] , S wins
if int(i) == 1 and computeranswer == 2:
    print("Computer Won, Sizor tears the Paper")
    print(f"""You:{userResponse}""")
    print(f"""Computer: {computerResponse}""")

# if P[1] against R[0], P wins
elif int(i) == 1 and computeranswer == 0:
    print("You won, Paper swollows the Rock")
    print(f"""You:{userResponse}""")
    print(f"""Computer: {computerResponse}""")

# if S[2] against R[0], R wins
elif int(i) == 2 and computeranswer == 0:
    print("Computer Won, Rock breaks the Sizor") 
    print(f"""You:{userResponse}""")
    print(f"""Computer: {computerResponse}""")

# if S[2] against P[1], S wins
elif int(i) == 2 and computeranswer == 1:
    print("You Won, Sizor tears the Paper")
    print(f"""You:{userResponse}""")
    print(f"""Computer: {computerResponse}""")

else:
    print("Invalid input")  