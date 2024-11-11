
myShoeList = ['Addidas', 'nike', 'Jordan', 'Puma']
myShoeList.append('Reebok') #append key word is used to add a new element in a List OR +=

tryNumberInteration = int(input("How many shoes do you want to try: "))
numberOftry = tryNumberInteration-1

while tryNumberInteration > 0:
    tryNumberInteration -= 1
    print(f"i have tried {myShoeList[tryNumberInteration]}")
