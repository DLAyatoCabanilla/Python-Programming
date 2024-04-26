print("The Love Calculator is calculating your score...")
name1 = input("Input the first name: ") # What is your name?
name2 = input("Input the second name: ") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combinedName = name1 + name2
combinedName = combinedName.lower()
tCount = combinedName.count("t")
rCount = combinedName.count("r")
uCount = combinedName.count("u")
eCount = combinedName.count("e")
true = tCount + rCount + uCount + eCount

lCount = combinedName.count("l")
oCount = combinedName.count("o")
vCount = combinedName.count("v")
eCount = combinedName.count("e")

love = lCount + oCount + vCount + eCount

score = f"{true}{love}"
scoreInt = int(score)

if scoreInt < 10 or scoreInt > 90:
  print(f"Your score is {scoreInt}, you go together like coke and mentos.")
elif scoreInt < 50 and scoreInt > 40:
  print(f"Your score is {scoreInt}, you are alright together.")
else:
  print(f"Your score is {scoreInt}.")

# print("The Love Calculator is calculating your score...")
# name1 = input()  # What is your name?
# name2 = input()  # What is their name?
# # Your code below this line 👇
# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e
#
# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e
#
# score = int(str(first_digit) + str(second_digit))
# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")