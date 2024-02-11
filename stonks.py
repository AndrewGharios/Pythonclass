#Sudent Name: Andrew Gharios
#Student ID: 1149366
#This progam is an investing calculator, it calculates your profits and losses when information is put in.


#input
name = input("Enter stock name: ")                   #inputs from user of data to be calculated.
shares = int(input("How many shares do you own in that company? "))
pricepershare = float(input("How much does each share cost? "))
sellprice = float(input("What is the new sell price? "))
commission = float(input("What is the commission? "))

#calculations                           
stockPaid = shares * pricepershare
paid_comm = stockPaid * commission                                #calculations using variables.
stockSold = shares * sellprice
sold_comm = stockSold * commission
profit = ( stockSold - sold_comm ) - (stockPaid + paid_comm)


#output
print()
print("Stock Name: ", name)
print("Amount paid for the stock: ", "$", format(stockPaid, '14.2f'))                    #Output with formatted numbers to have only 2 decimal spaces.
print("Commission paid on the purchase: ","$", format(paid_comm, '14.2f'))
print("Amount the stock sold for: ", "$",  format(stockSold, '14.2f'))
print("Commission paid on the sale: ", "$", format(sold_comm, '14.2f'))
print("Profit(or loss if negative): ", "$" , format(profit, '14.2f',))


##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\tax program.py =========
##Enter stock name: Lilys Virgin flowers
##How many shares do you own in that company? 192
##How much does each share cost? 50
##What is the new sell price? 400
##What is the commission? 0.34
##
##Stock Name:  Lilys Virgin flowers
##Amount paid for the stock:  $        9600.00
##Commission paid on the purchase:  $        3264.00
##Amount the stock sold for:  $       76800.00
##Commission paid on the sale:  $       26112.00
##Profit(or loss if negative):  $       37824.00
##>>> 
##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\tax program.py =========
##Enter stock name: Randy's wheel store
##How many shares do you own in that company? 102
##How much does each share cost? 450
##What is the new sell price? 395
##What is the commission? 1.23
##
##Stock Name:  Randy's wheel store
##Amount paid for the stock:  $       45900.00
##Commission paid on the purchase:  $       56457.00
##Amount the stock sold for:  $       40290.00
##Commission paid on the sale:  $       49556.70
##Profit(or loss if negative):  $     -111623.70
##>>> 
##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\tax program.py =========
##Enter stock name: Walt Disney Co.
##How many shares do you own in that company? 921
##How much does each share cost? 3495
##What is the new sell price? 4210
##What is the commission? 0.34
##
##Stock Name:  Walt Disney Co.
##Amount paid for the stock:  $     3218895.00
##Commission paid on the purchase:  $     1094424.30
##Amount the stock sold for:  $     3877410.00
##Commission paid on the sale:  $     1318319.40
##Profit(or loss if negative):  $    -1754228.70
##>>> 
##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\tax program.py =========
##Enter stock name: Nike Corp.
##How many shares do you own in that company? 30
##How much does each share cost? 3405
##What is the new sell price? 3409
##What is the commission? 0.45
##
##Stock Name:  Nike Corp.
##Amount paid for the stock:  $      102150.00
##Commission paid on the purchase:  $       45967.50
##Amount the stock sold for:  $      102270.00
##Commission paid on the sale:  $       46021.50
##Profit(or loss if negative):  $      -91869.00
##>>> 
##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\tax program.py =========
##Enter stock name: Death Row Records
##How many shares do you own in that company? 19
##How much does each share cost? 2940
##What is the new sell price? 1400
##What is the commission? 2.4
##
##Stock Name:  Death Row Records
##Amount paid for the stock:  $       55860.00
##Commission paid on the purchase:  $      134064.00
##Amount the stock sold for:  $       26600.00
##Commission paid on the sale:  $       63840.00
##Profit(or loss if negative):  $     -227164.00
##>>> 
