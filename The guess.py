import random
print("Give your interval: ")
def guess(y,x):
    c = [y,x]
    if y > x:
        y = c[1]
        x = c[0]
    print((f"Guess a number between {y} and {x}:"))
    random_nb = random.randint(y,x)
    guess = int(input())
    while guess != random_nb:
        if guess > random_nb:
            print("Too high! ")
            guess = int(input())
        else:
            print("Too low!")
            guess = int(input())
    print(f"You guessed right the number was {random_nb}")
guess(int(input()),int(input()))



