# Input a list of student scores
student_scores = input("Input the list of scores that you want to calculate the High Score: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highestScore = student_scores[0]
for score in student_scores:
  if score > highestScore:
    highestScore = score
print(f"The highest score in the class is: {highestScore}")

# highest_score = 0
# for score in student_scores:
#   if score > highest_score:
#     highest_score = score
#     # print(highest_score)
#
# print(f"The highest score in the class is: {highest_score}")