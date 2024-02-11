#Student Name: Andrew Gharios
#Student ID: 1149366
#This program finds sum and average of 3 numbers

#input data by user
name = input("What's your name? ")
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Second Number: "))

#processing/calculations
sum = num1 + num2 + num3
avg = sum / 3

#output
print()
print("Hey,", name)  
print("The sum is", sum)
print("The average is", avg)


#ask user to quit program
input("\n\nPresss any key to quit")


#5 test cases output
##============== RESTART: C:/Users/smgne/Desktop/Python CS 10/sumavg with input.py =============
##What's your name? Andrew
##Enter First Number: 123
##Enter Second Number: 15
##Enter Second Number: 51
##
##Hey,   Andrew
##The sum is 189
##The average is 63.0
##/n/nPresss any key to quit
##============== RESTART: C:/Users/smgne/Desktop/Python CS 10/sumavg with input.py =============
##What's your name? 1
##Enter First Number: 1
##Enter Second Number: 1
##Enter Second Number: 1
##
##Hey,   1
##The sum is 3
##The average is 1.0
##
##
##Presss any key to quit
##>>> 
##============== RESTART: C:/Users/smgne/Desktop/Python CS 10/sumavg with input.py =============
##What's your name? test
##Enter First Number: 1
##Enter Second Number: 2
##Enter Second Number: 3
##
##Hey, test
##The sum is 6
##The average is 2.0
##
##
##Presss any key to quit
