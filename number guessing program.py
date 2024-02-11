import random
#set mitial values
my_number = random.randint(1,100)
guess = int(input("Take a guess: "))
tries = 1

while guess != my_number:
    if guess > my_number:
        print("Lower...")
        else: print("Higher...")
        guess = int(input("Take another guess: "))
        tries = tries + 1

print("You got it! The number is", my_number)
print("You had",tries, "tries.")
