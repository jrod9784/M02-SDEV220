secret = 8
guess = input("Guess a number between 1 and 10: ")

if guess == secret:
    print("Just Right")
elif int(guess) > int(secret):
    print("Too High")
else:
    print("Too Low")
