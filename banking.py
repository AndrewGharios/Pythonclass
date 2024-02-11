#Sudent Name: Andrew Gharios
#Student ID: 1149366
#This program estimates your total and monthly payment based on your annual interest rate and loan amount.


#input data by user:
name = input("Hello worlder, what's your name? ")
annual_interest = float(input("What is your annual interest rate? "))           #User inputs name, annual interest rate, number of years and Loan amount.
numberOfYears = int(input("Enter number of years as a whole number: "))
loanAmount = float(input("What is your loan amount? "))     


#processing:
monthlyInterestRate = round(annual_interest / 1200, 2)  #calculating monthly interest rate using the annual interest rate inputed.
monthlyPayment = (loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12)))   
totalPayment = monthlyPayment * numberOfYears * 12

#output:
print()
print("Alright worlder, here's your monthly payment: ", format(monthlyPayment,',.2f'))  #Calculated and formatted output.
print("And your total payment is: ", format(totalPayment,',.2f'))                            

#program closing:
input("\n\nPay off your loan.")



#program testing:

##============ RESTART: C:/Users/smgne/Desktop/Python CS 10/banking.py ===========
##Hello worlder, what's your name? Derrick
##What is your annual interest rate? 10.23
##Enter number of years as a whole number: 12
##What is your loan amount? 45340.23
##
##Alright worlder, here's your monthly payment:  38,539.20
##And your total payment is:  5,549,644.80
##
##
##Pay off your loan.
##>>> 
##============ RESTART: C:/Users/smgne/Desktop/Python CS 10/banking.py ===========
##Hello worlder, what's your name? Lola
##What is your annual interest rate? 1.23
##Enter number of years as a whole number: 10
##What is your loan amount? 5430.30
##
##Alright worlder, here's your monthly payment:  543.04
##And your total payment is:  65,164.80
##
##
##Pay off your loan.
##>>> 
##============ RESTART: C:/Users/smgne/Desktop/Python CS 10/banking.py ===========
##Hello worlder, what's your name? Sandy
##What is your annual interest rate? 0.123
##Enter number of years as a whole number: 4
##What is your loan amount? 6504.20
##
##Alright worlder, here's your monthly payment:  171.28
##And your total payment is:  8,221.44
##
##
##Pay off your loan.
##>>> 
##============ RESTART: C:\Users\smgne\Desktop\Python CS 10\banking.py ===========
##Hello worlder, what's your name? Roland
##What is your annual interest rate? 8
##Enter number of years as a whole number: 10
##What is your loan amount? 3849.1
##
##Alright worlder, here's your monthly payment:  55.22
##And your total payment is:  6,626.40
##
##
##Pay off your loan.
##>>>
##=========== RESTART: C:\Users\smgne\Desktop\Python CS 10\banking.py ===========
##Hello worlder, what's your name? Andrew
##What is your annual interest rate? 94
##Enter number of years as a whole number: 10
##What is your loan amount? 1853.23
##
##Alright worlder, here's your monthly payment:  148.27
##And your total payment is:  17,792.40
##
##
##Pay off your loan.
##>>>
