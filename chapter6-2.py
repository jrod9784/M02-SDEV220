guess_me = 7
number = 0
while number != guess_me:
    number = input("Guess a number between 1 and 25 ")
    if int(number) > guess_me:
        print("OOps")
    elif int(number) < guess_me:
        print("Too Low")
    else:
        print("found it!")
        break
