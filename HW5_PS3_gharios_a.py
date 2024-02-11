#Andrew Gharios
#Student ID: 1449366
#This program calculates your loan when financing a car. 
class loan: #making a class for loan
      
    def __init__(self, irate , NumOfYear , amount , name):
        self.interestRate = irate
        self.years = NumOfYear
        self.amount = amount
        self.name = name

    def getInterestRate(self):
        return self.interestRate                        

    def getYears(self):
        return self.years

    def getAmount(self):
        return self.amount

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def setAmount(self,amount):
        self.amount = amount

    def setYears(self,years):
        self.years = years

    def setInterestRate(self,rate):
        self.interestRate = rate

    def getMonthlyPayment(self):
        monthlyInterestRate = self.interestRate / 1200
        monthlyPayment = self.amount * monthlyInterestRate / (1-(1 /(1 + monthlyInterestRate) ** (self.years * 12)))
        return monthlyPayment

    def getTotalPayment(self):
        return self.getMonthlyPayment() * self.years * 12

Loan = loan(0.0,0.0,0.0,"")
rate = float(input("Enter yearly interest rate: "))
Loan.setInterestRate(rate)
year = int(input("Enter number of year as as integer: "))    
Loan.setYears(year)
amount = float(input("Enter loan amount: "))
Loan.setAmount(amount)
name = input("Enter a borrower's name: ")
Loan.setName(name)
print("The loan is for", Loan.getName())
print("The monthly payment is %.2f" % Loan.getMonthlyPayment())
print("The total payment is %.2f" % Loan.getTotalPayment())

choice=input("\nDo you want to change the loan amount? Y for yes or enter to quit: ")
if choice == "Y" or choice == "y":              #If user enters Y, new amount replaces old one.
    newAmount=int(input("Enter the loan amount: "))
    Loan.setAmount(newAmount)
    print("The loan is for", Loan.getName())
    print("The monthly payment is %.2f" % Loan.getMonthlyPayment())
    print("The total payment is %.2f" % Loan.getTotalPayment())

#Test Cases

##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 5\HW5_PS3_gharios_a.py ====
##Enter yearly interest rate: 3.2
##Enter number of year as as integer: 4
##Enter loan amount: 13000.4
##Enter a borrower's name: Carmax
##The loan is for Carmax
##The monthly payment is 288.91
##The total payment is 13867.47
##
##Do you want to change the loan amount? Y for yes or enter to quit: y
##Enter the loan amount: 2
##The loan is for Carmax
##The monthly payment is 0.04
##The total payment is 2.13
##>>> 
##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 5\HW5_PS3_gharios_a.py ====
##Enter yearly interest rate: 1.2
##Enter number of year as as integer: 7
##Enter loan amount: 54430.45
##Enter a borrower's name: Mercedes Benz
##The loan is for Mercedes Benz
##The monthly payment is 675.90
##The total payment is 56775.72
##
##Do you want to change the loan amount? Y for yes or enter to quit:
##>>> 
##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 5\HW5_PS3_gharios_a.py ====
##Enter yearly interest rate: 4.4
##Enter number of year as as integer: 5
##Enter loan amount: 499500
##Enter a borrower's name: Housess
##The loan is for Housess
##The monthly payment is 9289.49
##The total payment is 557369.54
##
##Do you want to change the loan amount? Y for yes or enter to quit: 
##>>> 
##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 5\HW5_PS3_gharios_a.py ====
##Enter yearly interest rate: 1
##Enter number of year as as integer: 7
##Enter loan amount: 34550.67
##Enter a borrower's name: CarGurus
##The loan is for CarGurus
##The monthly payment is 426.05
##The total payment is 35788.44
##
##Do you want to change the loan amount? Y for yes or enter to quit:
##>>> 
