#Sudent Name: Andrew Gharios
#Student ID: 1149366
#HW 2, Set 2: Write a program that allows the user to input the followings as many times as he/she wants until the user is done (example it can be 5)

name = input("Enter stock name or -999 to quit: ") #inputs from user of data to be calculated.

while name != "-999":
    shares = int(input("How many shares do you own in that company? "))   #while loop
    pricepershare = float(input("How much does each share cost? "))
    sellprice = float(input("What is the new sell price? "))
    commission = float(input("What is the commission? "))                       
    stockPaid = shares * pricepershare
    paid_comm = stockPaid * commission                                #calculations using variables.
    stockSold = shares * sellprice
    sold_comm = stockSold * commission
    profit = ( stockSold - sold_comm ) - (stockPaid + paid_comm)
    print()
    print("Stock Name: ", name)
    print("Amount paid for the stock: \t\t", "$", format(stockPaid, '14,.2f'))                    #Output with formatted numbers to have only 2 decimal spaces.
    print("Commission paid on the purchase: \t","$", format(paid_comm, '14,.2f'))
    print("Amount the stock sold for: \t\t", "$",  format(stockSold, '14,.2f'))
    print("Commission paid on the sale: \t\t", "$", format(sold_comm, '14,.2f'))
    print("Profit(or loss if negative): \t\t", "$" , format(profit, '14,.2f',))
    print()
    name = input("Enter stock name or -999 to quit: ") #sentinel


##>>> 
##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW 1-2.py =========
##Enter stock name or -999 to quit: Derrick Inc
##How many shares do you own in that company? 1094
##How much does each share cost? 40
##What is the new sell price? 80
##What is the commission? 0.2
##
##Stock Name:  Derrick Inc
##Amount paid for the stock: 		 $      43,760.00
##Commission paid on the purchase: 	 $       8,752.00
##Amount the stock sold for: 		 $      87,520.00
##Commission paid on the sale: 		 $      17,504.00
##Profit(or loss if negative): 		 $      17,504.00
##
##Enter stock name or -999 to quit: Vans
##How many shares do you own in that company? 2049
##How much does each share cost? 43
##What is the new sell price? 63
##What is the commission? 0.03
##
##Stock Name:  Vans
##Amount paid for the stock: 		 $      88,107.00
##Commission paid on the purchase: 	 $       2,643.21
##Amount the stock sold for: 		 $     129,087.00
##Commission paid on the sale: 		 $       3,872.61
##Profit(or loss if negative): 		 $      34,464.18
##
##Enter stock name or -999 to quit: -999
##>>> 
##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW 1-2.py =========
##Enter stock name or -999 to quit: Fast Gas
##How many shares do you own in that company? 10
##How much does each share cost? 10049
##What is the new sell price? 10345
##What is the commission? 0.003
##
##Stock Name:  Fast Gas
##Amount paid for the stock: 		 $     100,490.00
##Commission paid on the purchase: 	 $         301.47
##Amount the stock sold for: 		 $     103,450.00
##Commission paid on the sale: 		 $         310.35
##Profit(or loss if negative): 		 $       2,348.18
##
##Enter stock name or -999 to quit: CheapIphones
##How many shares do you own in that company? 58
##How much does each share cost? 100
##What is the new sell price? 30
##What is the commission? 0.02
##
##Stock Name:  CheapIphones
##Amount paid for the stock: 		 $       5,800.00
##Commission paid on the purchase: 	 $         116.00
##Amount the stock sold for: 		 $       1,740.00
##Commission paid on the sale: 		 $          34.80
##Profit(or loss if negative): 		 $      -4,210.80
##
##Enter stock name or -999 to quit: -999
##>>> 
##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW 1-2.py =========
##Enter stock name or -999 to quit: Doggiz
##How many shares do you own in that company? 127
##How much does each share cost? 4577432
##What is the new sell price? 9299123
##What is the commission? 0.3
##
##Stock Name:  Doggiz
##Amount paid for the stock: 		 $ 581,333,864.00
##Commission paid on the purchase: 	 $ 174,400,159.20
##Amount the stock sold for: 		 $ 1,180,988,621.00
##Commission paid on the sale: 		 $ 354,296,586.30
##Profit(or loss if negative): 		 $  70,958,011.50
##
##Enter stock name or -999 to quit: -999
##>>> 
##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW 1-2.py =========
##Enter stock name or -999 to quit: Rentacar
##How many shares do you own in that company? 49
##How much does each share cost? 5
##What is the new sell price? 3
##What is the commission? 2
##
##Stock Name:  Rentacar
##Amount paid for the stock: 		 $         245.00
##Commission paid on the purchase: 	 $         490.00
##Amount the stock sold for: 		 $         147.00
##Commission paid on the sale: 		 $         294.00
##Profit(or loss if negative): 		 $        -882.00
##
##Enter stock name or -999 to quit: Glass inc.
##How many shares do you own in that company? 543
##How much does each share cost? 14
##What is the new sell price? 8
##What is the commission? 0.09
##
##Stock Name:  Glass inc.
##Amount paid for the stock: 		 $       7,602.00
##Commission paid on the purchase: 	 $         684.18
##Amount the stock sold for: 		 $       4,344.00
##Commission paid on the sale: 		 $         390.96
##Profit(or loss if negative): 		 $      -4,333.14
##
##Enter stock name or -999 to quit: -999
##>>>
##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW2_PS2_gharios_a.py ====
##Enter stock name or -999 to quit: HP computers
##How many shares do you own in that company? 219
##How much does each share cost? 59420
##What is the new sell price? 59659
##What is the commission? 0.01
##
##Stock Name:  HP computers
##Amount paid for the stock: 		 $  13,012,980.00
##Commission paid on the purchase: 	 $     130,129.80
##Amount the stock sold for: 		 $  13,065,321.00
##Commission paid on the sale: 		 $     130,653.21
##Profit(or loss if negative): 		 $    -208,442.01
##
##Enter stock name or -999 to quit: Honda
##How many shares do you own in that company? 20
##How much does each share cost? 100293
##What is the new sell price? 10001
##What is the commission? 0.01
##
##Stock Name:  Honda
##Amount paid for the stock: 		 $   2,005,860.00
##Commission paid on the purchase: 	 $      20,058.60
##Amount the stock sold for: 		 $     200,020.00
##Commission paid on the sale: 		 $       2,000.20
##Profit(or loss if negative): 		 $  -1,827,898.80
##
##Enter stock name or -999 to quit: -999
##>>> 
