import random as R

again = True

while again:
    print(R.randint(1, 6))
    another_roll = input("Wanna roll the dice again? (y/n): ")
    if another_roll.lower() == "y":
        continue
    else:
        break

