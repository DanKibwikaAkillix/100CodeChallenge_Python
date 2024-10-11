# Variables
# We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. Write 3 lines of code to switch the contents of the variables. You are not allowed to type the words "milk" or "juice". You are only allowed to use variables to solve this exercise.

glass1 = "milk"
glass2 = "juice"

# Imagine you actually have a glass of milk and a glass of juice. How can you switch out the liquids in real life?

# Solution

# get a 3rd glass,
# the juice in glass2 goes to glass3
# the milk in glass1 goes to glass2
# and then the juice in glass3 goes to glass1

glass1 = "milk"
glass2 = "juice"
glass3 = ""

glass3 = glass2
glass2 = glass1
glass1 = glass3