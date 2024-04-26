# Enter your height in meters e.g., 1.55
height = float(input("What is your height in meters? "))
# Enter your weight in kilograms e.g., 72
weight = int(input("What is your weight in Kilograms? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bodyMassIndex = weight / height ** 2
if bodyMassIndex < 18.5:
  print(f"Your BMI is {bodyMassIndex}, you are underweight.")
elif bodyMassIndex < 25:
  print(f"Your BMI is {bodyMassIndex}, you have a normal weight.")
elif bodyMassIndex >= 25 and bodyMassIndex < 30:
  print(f"Your BMI is {bodyMassIndex}, you are slightly overweight.")
elif bodyMassIndex >= 30 and bodyMassIndex < 35:
  print(f"Your BMI is {bodyMassIndex}, you are obese.")
elif bodyMassIndex >= 35:
  print(f"Your BMI is {bodyMassIndex}, you are clinically obese.")
else:
  print(f"Your BMI is {bodyMassIndex}, you are clinically obese.")

# height = float(input())  # in meters e.g., 1.55
# weight = int(input())  # in kilograms e.g., 72
# # Your code below this line 👇
# bmi = weight / (height * height)
# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")
