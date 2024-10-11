# check the length of a string
# len("Hello")

# check the data_type of a variable
print(type(123))
print(type("Hello"))
print(type(123.02))
print(type(True))


# covert from one type to an other cast to the target type

n = int("123") 
print(n)

# but we can't convert a string to a float or a int

n2 = float("Abvd")
n3 = int("Abc")

# we get this a type erro :

# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PYTHON_COURSE\Day2\1_functions.py", line 18, in <module>
#     n2 = float("Abvd")
#          ^^^^^^^^^^^^^
# ValueError: could not convert string to float: 'Abvd'

# FIX THE BUG, IN THIS CODE 

# print("Number of letters in your name:" +len(input("What is your name?")))

# solution 

name_input = input("What is your name?")
lengh_name = len(name_input)
print(type(lengh_name))

# covert to string
length_str = str(lengh_name)
print("Number of letters in your name:"+ length_str  )