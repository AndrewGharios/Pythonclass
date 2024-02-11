#Sudent Name: Andrew Gharios
#Student ID: 1149366
#This program finds the number of ingredients needed to bake a inputed amount of cookies.

#Data:(Given)
sugar1 = 1.5 / 48    #cups of sugar, butter and flour per 1 cookie according to given data
butter1 = 1 / 48
flour1 = 2.75 / 48


#input data by user:
name = input("Hello Chef, what's your name? ")       #name and number of cookies input by user.
cookies = int(input("How many cookies would you like to make? "))

              
#processing:
sugar = round(cookies * float(sugar1), 2)
butter = round(cookies * float(butter1), 2)     #times the number of cookies to the number of sugar, butter and flour needed per 1 cookie.
flour = round(cookies * float(flour1), 2)
              
#output:
print()
print("Ok Chef,", name)
print("To make " + str(cookies) + " cookies you will need:")
print("cups of sugar: ", float(sugar))
print("cups of butter: ", float(butter))
print("cups of flour: ", float(flour))

#Closing program
input("\n\nHappy baking!")


#Testing:
##================= RESTART: C:/Users/smgne/Desktop/Python CS 10/cookie maker.py ================
##Hello Chef, what's your name? Andrew
##How many cookies would you like to make? 12
##
##Ok Chef, Andrew
##To make 12 cookies you will need:
##cups of sugar:  0.38
##cups of butter:  0.25
##cups of flour:  0.69
##
##
##Happy baking!
##>>> Teddy
##Traceback (most recent call last):
##  File "<pyshell#1>", line 1, in <module>
##    Teddy
##NameError: name 'Teddy' is not defined
##>>> 
##>>> 
##================= RESTART: C:/Users/smgne/Desktop/Python CS 10/cookie maker.py ================
##Hello Chef, what's your name? Teddy
##How many cookies would you like to make? 41
##
##Ok Chef, Teddy
##To make 41 cookies you will need:
##cups of sugar:  1.28
##cups of butter:  0.85
##cups of flour:  2.35
##
##
##Happy baking!
##>>> 
##>>> 
##================= RESTART: C:/Users/smgne/Desktop/Python CS 10/cookie maker.py ================
##Hello Chef, what's your name? Lora
##How many cookies would you like to make? 85
##
##Ok Chef, Lora
##To make 85 cookies you will need:
##cups of sugar:  2.66
##cups of butter:  1.77
##cups of flour:  4.87
##
##
##Happy baking!
##>>>
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\cookie maker.py =========
##Hello Chef, what's your name? Devin
##How many cookies would you like to make?  129
##
##Ok Chef, Devin
##To make 129 cookies you will need:
##cups of sugar:  4.03
##cups of butter:  2.69
##cups of flour:  7.39
##
##
##Happy baking!
##>>> 
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\cookie maker.py =========
##Hello Chef, what's your name? Erick
##How many cookies would you like to make? 213
##
##Ok Chef, Erick
##To make 213 cookies you will need:
##cups of sugar:  6.66
##cups of butter:  4.44
##cups of flour:  12.2
