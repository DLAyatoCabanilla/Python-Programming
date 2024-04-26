# Which year do you want to check?
year = int(input("Enter the year you want to check if it's a leap year or not: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f" The year {year} is a Leap year")
else:
    print(f"The year {year} is NOT a leap year")

# # Which year do you want to check?
# year = int(input())
#
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("Leap year")
# else:
#   print("Not leap year")
