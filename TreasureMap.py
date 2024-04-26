line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ") # Where do you want to put the treasure?

letter = position[0].upper()
letterABC = ["A", "B", "C"]
letterIndex = letterABC.index(letter)
numberIndex = int(position[1]) - 1
map[numberIndex][letterIndex] = 'X'


print(f"{line1}\n{line2}\n{line3}")