# Input a Python list of student heights
student_heights = input("Input the height of each student: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Code below this row 👇
total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")
number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")
average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")

# # Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
#
# # Write your code below this row 👇
# totalHeight = 0
# numberOfStudents = 0
#
# for height in student_heights:
#   totalHeight = totalHeight + height
#   numberOfStudents += 1
#
# print(f"total height = {totalHeight}")
# print(f"number of students = {numberOfStudents}")
#
# averageHeight = round(totalHeight / numberOfStudents)
# print(f"average height = {averageHeight}")