from operator import truediv


choice = input("Enter one of four options: Cherry, Pea, Watermelon, Pumpkin")
small = True
green = False

if choice == "Cherry":
    small = True
    green = False
elif choice == "Pea":
    small = True
    green = True
elif choice == "Watermelon":
    small = False
    green = True
elif choice == "Pumpkin":
    small = False
    green = False
else:
    print("Choice not recognized")
