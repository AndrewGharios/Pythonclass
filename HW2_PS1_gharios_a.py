#Sudent Name: Andrew Gharios
#Student ID: 1149366
#HW 2, PS1 :Write a program that allows the user to input the followings as many times as he/she wants until the user is done. 

import random      #import random in order to generate lottery winning numbers
lottery = random.randint(10,99)   
guess = int(input("Input a single two digits number: "))   
win = 0  #statement for no repetitions

 
while guess != -999:                 #while loop so user can play as much as they want.
    right_guess = guess // 10
    left_guess = guess % 10                
    right_lottery = lottery // 10
    left_lottery = lottery % 10
    if lottery == guess:
        win = 1
        print("You win $10,000")  
    if left_guess == right_lottery and right_guess == left_lottery and win != 1:                           #winning condition ifs
        win = 1
        print("You win $3,000")
    if left_guess == left_lottery and win != 1 or right_guess == right_lottery and win != 1 or right_guess == left_lottery and win != 1 or left_guess == right_lottery and win != 1:
        win = 1
        print("You win $1,000")
    win = 0      
    guess = int(input("Input a single two digits number, or enter -999 to quit: "))   #sentinel

##>>> 
##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW2_PS1_gharios_a.py ====
##Input a single two digits number: 23
##Input a single two digits number, or enter -999 to quit: 48
##Input a single two digits number, or enter -999 to quit: 39
##Input a single two digits number, or enter -999 to quit: 40
##Input a single two digits number, or enter -999 to quit: 22
##Input a single two digits number, or enter -999 to quit: 12
##You win $1,000
##Input a single two digits number, or enter -999 to quit: 85
##Input a single two digits number, or enter -999 to quit: 23
##Input a single two digits number, or enter -999 to quit: 19
##You win $1,000
##Input a single two digits number, or enter -999 to quit: 17
##You win $3,000
##Input a single two digits number, or enter -999 to quit: 71
##You win $10,000
##Input a single two digits number, or enter -999 to quit: -999
##>>> 
##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW2_PS1_gharios_a.py ====
##Input a single two digits number: 38
##Input a single two digits number, or enter -999 to quit: 49
##Input a single two digits number, or enter -999 to quit: 592
##Input a single two digits number, or enter -999 to quit: 2
##Input a single two digits number, or enter -999 to quit: 3
##Input a single two digits number, or enter -999 to quit: 4
##Input a single two digits number, or enter -999 to quit: 
##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW2_PS1_gharios_a.py ====
##Input a single two digits number: 23
##You win $1,000
##Input a single two digits number, or enter -999 to quit: 32
##You win $1,000
##Input a single two digits number, or enter -999 to quit: 33
##You win $1,000
##Input a single two digits number, or enter -999 to quit: 31
##You win $1,000
##Input a single two digits number, or enter -999 to quit: 23
##You win $1,000
##Input a single two digits number, or enter -999 to quit: -999
##>>>
##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW2_PS1_gharios_a.py ====
##Input a single two digits number: 49
##Input a single two digits number, or enter -999 to quit: 58
##You win $1,000
##Input a single two digits number, or enter -999 to quit: 59
##You win $1,000
##Input a single two digits number, or enter -999 to quit: 53
##You win $1,000
##Input a single two digits number, or enter -999 to quit: 50
##You win $1,000
##Input a single two digits number, or enter -999 to quit: 39
##Input a single two digits number, or enter -999 to quit: 48
##Input a single two digits number, or enter -999 to quit: 13
##Input a single two digits number, or enter -999 to quit: 12
##You win $1,000
##Input a single two digits number, or enter -999 to quit: 11
##Input a single two digits number, or enter -999 to quit: 52
##You win $10,000
##Input a single two digits number, or enter -999 to quit: 25
##You win $3,000
##Input a single two digits number, or enter -999 to quit: -999
##>>> 
##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW2_PS1_gharios_a.py ====
##Input a single two digits number: 33
##Input a single two digits number, or enter -999 to quit: 28
##You win $1,000
##Input a single two digits number, or enter -999 to quit: 59
##Input a single two digits number, or enter -999 to quit: 49
##Input a single two digits number, or enter -999 to quit: 12
##You win $1,000
##Input a single two digits number, or enter -999 to quit: 28
##You win $1,000
##Input a single two digits number, or enter -999 to quit: 29
##You win $1,000
##Input a single two digits number, or enter -999 to quit: 40
##Input a single two digits number, or enter -999 to quit: 11
##Input a single two digits number, or enter -999 to quit: 19
##Input a single two digits number, or enter -999 to quit: 49
##Input a single two digits number, or enter -999 to quit: 32
##You win $1,000
##Input a single two digits number, or enter -999 to quit: 12
##You win $1,000
##Input a single two digits number, or enter -999 to quit: 94
##Input a single two digits number, or enter -999 to quit: 01
##Input a single two digits number, or enter -999 to quit: 10
##Input a single two digits number, or enter -999 to quit: 49
##Input a single two digits number, or enter -999 to quit: -999
##>>> 
