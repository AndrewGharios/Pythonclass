#input
stars_numb = int(input("How many stars do you want? "))
stars = "*"                                              #preset for our stars and how many times we need to print them.

#ouput/calculations
while stars_numb > 0:               #opening the loop by making sure theres more than 0 stars for the program to make sense.
    display = stars_numb * stars   
    print(display)
    stars_numb = -1             #closing the loop by setting the while value to -1.

#tests:

##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB 1/lab 1-5.py ========
##How many stars do you want? 1
##*
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB 1/lab 1-5.py ========
##How many stars do you want? 10
##**********
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB 1/lab 1-5.py ========
##How many stars do you want? 49
##*************************************************
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB 1/lab 1-5.py ========
##How many stars do you want? 94
##**********************************************************************************************
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB 1/lab 1-5.py ========
##How many stars do you want? -1
##>>> 
