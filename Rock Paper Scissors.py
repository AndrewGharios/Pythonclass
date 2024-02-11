import random

print("Alright motherfuckers, rock paper, skizerz" )
count = 0
#teacher's way

import random

user_num = int(input("Scissors(0), Rock(1) , Paper(0): "))

while user_num != -999:
    comp_num = random.randint(0,2)
    
    if comp_num == 0:
        if user_num == 0:
            print("Draw")
        elif user_num == 1:
                print("You won")
                count = count + 1
        elif user_num == 2:
                    print("You lose")
                    count = count - 1
    elif comp_num == 1:
        if user_num == 0:
            print("You lose")
            count = count - 1
        elif user_num == 1:
            print("Draw")
        elif user_num == 2:
            print("You won")
            count = count + 1

    elif comp_num == 2:
        if user_num == 0:
            print("You won")
            count = count + 1
        elif user_num == 1:
            print("You lost")
            count = count - 1
        elif user_num == 2:
            print("Draw")
    user_num = int(input("Choose another one to play again, or type -999 to quit: "))
 

if count > 2:
    print("You won, you're score is: ", count)
if count < 2:
    print("You lost, you're score is: ",count)
if count == 0:
    print("Draw")

input("Press enter to quit")
    
        
