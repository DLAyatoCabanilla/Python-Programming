# 1st input: enter height in meters e.g: 1.65
height = input("What is your height? ")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("What is your weight? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
newHeight = float(height)
newWeight = int(weight)
bodyMassIndex = newWeight / (newHeight * newHeight)
print(f"Your Body Mass Index is {bodyMassIndex}")
bodyMassIndex = int(bodyMassIndex)
bodyMassIndex = str(bodyMassIndex)
print("Your Rounded Body Mass Index is " + bodyMassIndex)

# or the code below
# height = input()
# weight = input()
# # Your code below this line 👇
# weight_as_int = int(weight)
# height_as_float = float(height)
# # Using the exponent operator **
# bmi = weight_as_int / height_as_float ** 2
# # or using multiplication and PEMDAS
# bmi = weight_as_int / (height_as_float * height_as_float)
#
# bmi_as_int = int(bmi)
# print(bmi_as_int)


