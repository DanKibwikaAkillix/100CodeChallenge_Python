# student_score = input("Enter the score of the student: ").split()
# for n in range(0, len(student_score)):
#     student_score[n] = int(student_score[n])
# print(student_score)

# for score in student_score:
#     if score > student_score[n]:
#        i = score
# print(f"The highest score in the class is: {i}")

    # 78 65 89 55 91 64 89

    # or better:

student_score = input("Enter the score of the student: ").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")