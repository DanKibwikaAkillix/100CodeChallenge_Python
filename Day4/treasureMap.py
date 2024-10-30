row1 = ["🏵","🏵" , "🏵" ]
row2 = ["🏵","🏵" , "🏵" ]
row3 = ["🏵","🏵" , "🏵" ]
#🤍

map =  [row1, row2, row3]
# print(map)
print(f"{row1}\n{row2}\n{row3}")

# boxSIZE = len()
question = input("Where do you want to put the Treasure ?:.....")
answerSplit = question.split(",")

rowOfTreasureIs = int(answerSplit[0])-1
columnOfTreasureIs = int(answerSplit[1])-1


rowSelected = map[rowOfTreasureIs]
rowSelected [columnOfTreasureIs] = "🤍"

print(f"{row1}\n{row2}\n{row3}")