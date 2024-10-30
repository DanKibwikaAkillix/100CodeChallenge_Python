
import random

myFriend = input('Enter your friends names ?:......')
myFriendSplit = myFriend.split(', ')
friendListLen = len(myFriendSplit)

print(myFriendSplit)
print(f'so you gusy are {friendListLen } So who is paying the bill today? ROLLL ROOLLL ROOLL ROOOOLLLL: ....')


answer = random.randint(0,friendListLen-1)
candidate = myFriendSplit[answer]
print(f"The lucky one is {candidate}")