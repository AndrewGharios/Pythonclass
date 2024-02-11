#Andrew Gharios
#Student ID: 1149366
#HW 3, Set 3: Stocks program from homework 2 with functions applied.

#function to get user input
def getStock()->(str,int,float,float,float):
    '''This function acquires user input and stores it in the memory'''
    name = input("Enter stock name: ") #inputs from user of data to be calculated.
    shares = int(input("How many shares do you own in that company? ")) 
    pricepershare = float(input("How much does each share cost? "))
    sellprice = float(input("What is the new sell price? "))
    commission = float(input("What is the commission? "))
    
    return name,shares,pricepershare ,sellprice,commission

#function to calculate different amounts and commsisions
def calculate(shares:int,pricepershare:float,sellprice:float,commission:float)->(float,float,float,float,float):
    '''This function calculates and computes the input given'''
    stockPaid = shares * pricepershare
    paid_comm = stockPaid * commission                                #calculations using variables.
    stockSold = shares * sellprice
    sold_comm = stockSold * commission
    profit = ( stockSold - sold_comm ) - (stockPaid + paid_comm)
  
  
    return stockPaid,paid_comm,stockSold,sold_comm,profit
  
#function to display all the calculated amounts and commissions
def display(name:str,stockPaid:float,paid_comm:float,stockSold:float,sold_comm:float,profit:float):
    '''This function is displays all the calculated numbers'''
    print("\n_________STOCK DETAILS________\n")
    print()
    print("Stock Name: ", name)
    print("Amount paid for the stock: \t\t", "$", format(stockPaid, '14,.2f'))                    #Output with formatted numbers to have only 2 decimal spaces.
    print("Commission paid on the purchase: \t","$", format(paid_comm, '14,.2f'))
    print("Amount the stock sold for: \t\t", "$",  format(stockSold, '14,.2f'))
    print("Commission paid on the sale: \t\t", "$", format(sold_comm, '14,.2f'))
    if(profit<0):
        print("Loss:  \t\t\t\t\t", "$" , format(profit, '14,.2f',))
    else:
        print("Profit:  \t\t\t\t", "$" , format(profit, '14,.2f',))

def main():
    while(True): #while loop to repeat choice if wanted by user
        loop=input("Do you want to enter stock details?(Y/N): ")
        if(loop == "N" or loop == "n"):
            break
        name,shares,price,sellingPrice,commission = getStock()
        amtSpend,comSpend,amtSold,comSold,moneyDiff = calculate(shares,price,sellingPrice,commission)
        display(name,amtSpend,comSpend,amtSold,comSold,moneyDiff)
        
if __name__=="__main__":
    main()

##==== RESTART: C:/Users/smgne/Desktop/Python CS 10/HW 3/HW3_PS1_Gharios_A.py ====
##Do you want to enter stock details?(Y/N): y
##Enter stock name: Derrick inc.
##How many shares do you own in that company? 120
##How much does each share cost? 349
##What is the new sell price? 340
##What is the commission? 0.02
##
##_________STOCK DETAILS________
##
##
##Stock Name:  Derrick inc.
##Amount paid for the stock: 		 $      41,880.00
##Commission paid on the purchase: 	 $         837.60
##Amount the stock sold for: 		 $      40,800.00
##Commission paid on the sale: 		 $         816.00
##Loss:  					 $      -2,733.60
##Do you want to enter stock details?(Y/N): y
##Enter stock name: Paintball
##How many shares do you own in that company? 20
##How much does each share cost? 4950
##What is the new sell price? 5020
##What is the commission? 0.09
##
##_________STOCK DETAILS________
##
##
##Stock Name:  Paintball
##Amount paid for the stock: 		 $      99,000.00
##Commission paid on the purchase: 	 $       8,910.00
##Amount the stock sold for: 		 $     100,400.00
##Commission paid on the sale: 		 $       9,036.00
##Loss:  					 $     -16,546.00
##Do you want to enter stock details?(Y/N): n
##>>> 
##==== RESTART: C:/Users/smgne/Desktop/Python CS 10/HW 3/HW3_PS1_Gharios_A.py ====
##Do you want to enter stock details?(Y/N): y
##Enter stock name: Ferrari
##How many shares do you own in that company? 2
##How much does each share cost? 100454
##What is the new sell price? 102405
##What is the commission? 0.04
##
##_________STOCK DETAILS________
##
##
##Stock Name:  Ferrari
##Amount paid for the stock: 		 $     200,908.00
##Commission paid on the purchase: 	 $       8,036.32
##Amount the stock sold for: 		 $     204,810.00
##Commission paid on the sale: 		 $       8,192.40
##Loss:  					 $     -12,326.72
##Do you want to enter stock details?(Y/N): y
##Enter stock name: Lamborghini
##How many shares do you own in that company? 245
##How much does each share cost? 14055
##What is the new sell price? 17034
##What is the commission? 0.02
##
##_________STOCK DETAILS________
##
##
##Stock Name:  Lamborghini
##Amount paid for the stock: 		 $   3,443,475.00
##Commission paid on the purchase: 	 $      68,869.50
##Amount the stock sold for: 		 $   4,173,330.00
##Commission paid on the sale: 		 $      83,466.60
##Profit:  				 $     577,518.90
##Do you want to enter stock details?(Y/N): n
##>>> 
##==== RESTART: C:/Users/smgne/Desktop/Python CS 10/HW 3/HW3_PS1_Gharios_A.py ====
##Do you want to enter stock details?(Y/N): y
##Enter stock name: American Tires
##How many shares do you own in that company? 3
##How much does each share cost? 240
##What is the new sell price? 500
##What is the commission? 3
##
##_________STOCK DETAILS________
##
##
##Stock Name:  American Tires
##Amount paid for the stock: 		 $         720.00
##Commission paid on the purchase: 	 $       2,160.00
##Amount the stock sold for: 		 $       1,500.00
##Commission paid on the sale: 		 $       4,500.00
##Loss:  					 $      -5,880.00
##Do you want to enter stock details?(Y/N): y
##Enter stock name: Olymipcs
##How many shares do you own in that company? 495
##How much does each share cost? 20323
##What is the new sell price? 23333
##What is the commission? 0.001
##
##_________STOCK DETAILS________
##
##
##Stock Name:  Olymipcs
##Amount paid for the stock: 		 $  10,059,885.00
##Commission paid on the purchase: 	 $      10,059.89
##Amount the stock sold for: 		 $  11,549,835.00
##Commission paid on the sale: 		 $      11,549.84
##Profit:  				 $   1,468,340.28
##Do you want to enter stock details?(Y/N): n
##>>> 
##==== RESTART: C:/Users/smgne/Desktop/Python CS 10/HW 3/HW3_PS1_Gharios_A.py ====
##Do you want to enter stock details?(Y/N): Y
##Enter stock name: SanDals
##How many shares do you own in that company? 5600
##How much does each share cost? 34
##What is the new sell price? 38
##What is the commission? 0.001
##
##_________STOCK DETAILS________
##
##
##Stock Name:  SanDals
##Amount paid for the stock: 		 $     190,400.00
##Commission paid on the purchase: 	 $         190.40
##Amount the stock sold for: 		 $     212,800.00
##Commission paid on the sale: 		 $         212.80
##Profit:  				 $      21,996.80
##Do you want to enter stock details?(Y/N): n
##>>>
##==== RESTART: C:/Users/smgne/Desktop/Python CS 10/HW 3/HW3_PS1_Gharios_A.py ====
##Do you want to enter stock details?(Y/N): Y
##Enter stock name: HP laptops
##How many shares do you own in that company? 23
##How much does each share cost? 3459
##What is the new sell price? 3000
##What is the commission? 0
##
##_________STOCK DETAILS________
##
##
##Stock Name:  HP laptops
##Amount paid for the stock: 		 $      79,557.00
##Commission paid on the purchase: 	 $           0.00
##Amount the stock sold for: 		 $      69,000.00
##Commission paid on the sale: 		 $           0.00
##Loss:  					 $     -10,557.00
##Do you want to enter stock details?(Y/N): Y
##Enter stock name: Glassez
##How many shares do you own in that company? 100
##How much does each share cost? 495
##What is the new sell price? 599
##What is the commission? 4
##
##_________STOCK DETAILS________
##
##
##Stock Name:  Glassez
##Amount paid for the stock: 		 $      49,500.00
##Commission paid on the purchase: 	 $     198,000.00
##Amount the stock sold for: 		 $      59,900.00
##Commission paid on the sale: 		 $     239,600.00
##Loss:  					 $    -427,200.00
##Do you want to enter stock details?(Y/N): n
##>>> 
