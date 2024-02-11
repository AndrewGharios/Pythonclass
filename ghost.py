import random
score = 0
ghost = random.randint(1, 3)
print("Ghost Game!")
print("There's 3 doors and the ghost is inside one of them.")
answer = int(input("Choose a door number: "))

while answer != ghost:
             ghost = random.randint(1, 3)
             score = score + 1
             print("No ghost here! Procceed to the next room.")
             answer = int(input("Choose another door: "))

print("Boo!")
print("Your score is: ", score) 


##Teacher notes:
##    
##random.randint(1, 3)
##Guess which door
##If statement to compare
##If match found not continue
