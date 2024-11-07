
studentHeight = input('Enter the student height?:....').split()
for n in range(0, len(studentHeight)):
    studentHeight[n] = int(studentHeight[n])
add = sum(studentHeight)
mean = add/ len(studentHeight)
print(round(mean,0))

# without using the sum function and add function 

studentHeight = input('Enter the student height?:....').split()
for n in range(0, len(studentHeight)):
    studentHeight[n] = int(studentHeight[n])

total_height = 0
for height in studentHeight:
    total_height += height

total_student = len(studentHeight)
mean = total_height/total_student
print(round(mean, 0))
