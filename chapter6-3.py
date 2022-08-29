guess_me = 5
number = 0
print(number)
for num in range(10):
    if num == guess_me:
        print("found it!")
        break
    elif num < guess_me:
        print("Too low")
        number += 1
    else:
        print("oops")
print(number)
