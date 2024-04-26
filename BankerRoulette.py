names_string = input("Enter The Names of your Banker: ")
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
# moreNames = ["Harry", "James", "Jack"]
# names.extend(moreNames)
randomIndex = random.randint(0, len(names) - 1)
selectedIndex = names[randomIndex]
print(selectedIndex + " is going to buy the meal today!")
# names = names_string.split(", ")
#
# import random
#
# # Get the total number of items in list.
# num_items = len(names)
# # Generate random numbers between 0 and the last index.
# random_choice = random.randint(0, num_items - 1)
# # Choose and print a random name.
# print(names[random_choice])
