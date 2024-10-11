# it's binary operator, that returns the remaining of a divition
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
modulo = int(a % b)
print(f"The result is:....{modulo} \n\n")


if modulo == 0:
   print(f"and your First number: {a} is Even")

else:
    print(f"the number {a} is Odd")