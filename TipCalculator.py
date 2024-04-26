# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill of your purchase? "))
percentageTip = int(input("What percentage tip would you like to give? "))
splitTheBill = int(input("How many people would you like to split the bill even to? "))
# calculations created below 👇
newPercentageTip = percentageTip / 100
totalBill = bill * newPercentageTip
newTotalBill = bill + totalBill
newTip = newTotalBill / splitTheBill
round(newTip, 2)
print(f"Each person should pay: ${newTip:.2f}")
# or
# newTip = "{:.2f}".format(newTip)



