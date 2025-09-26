import random

secret = random.randint(1, 100)

guess = int(input("Enter a number: "))
print("You guessed: ", guess)


while guess != secret:
    if guess < secret:
        print("Too Low")
    elif guess > secret:
        print("Too High")
    guess = int(input("Enter a number: "))
else:
    print("Congrats! you've got it")