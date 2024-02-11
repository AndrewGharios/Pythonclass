#Andrew Gharios
#Student ID: 1149366
#HW 2, Set 3: Convert program 2 codes to use For loops to enter stocks data and output the stocks data. You are to ask the user how many stocks does he/she wants to input.


#input
Nstocks = int(input("How many stocks do you want to enter? "))   #input question


#calculations
for index in range(Nstocks):      #for loop to keep looping as many times as user needs.
    name = input("Enter stock name: ")
    shares = int(input("How many shares do you own in that company? "))
    pricepershare = float(input("How much does each share cost? "))
    sellprice = float(input("What is the new sell price? "))
    commission = float(input("What is the commission? "))                       
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
    print()     

###>>> 
##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW2_PS3_gharios_a.py ====
##How many stocks do you want to enter? 2
##Enter stock name: Test
##How many shares do you own in that company? 12823
##How much does each share cost? 38238
##What is the new sell price? 38
##What is the commission? 0.09
##
##Stock Name:  Test
##Amount paid for the stock:  $   490325874.00
##Commission paid on the purchase:  $    44129328.66
##Amount the stock sold for:  $      487274.00
##Commission paid on the sale:  $       43854.66
##Profit(or loss if negative):  $  -534011783.32
##
##Enter stock name: Deresl
##How many shares do you own in that company? 123
##How much does each share cost? 1245
##What is the new sell price? 1900
##What is the commission? 0.02
##
##Stock Name:  Deresl
##Amount paid for the stock:  $      153135.00
##Commission paid on the purchase:  $        3062.70
##Amount the stock sold for:  $      233700.00
##Commission paid on the sale:  $        4674.00
##Profit(or loss if negative):  $       72828.30
##
##>>>
##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW2_PS3_gharios_a.py ====
##How many stocks do you want to enter? 2
##Enter stock name: Tenisballs inc.
##How many shares do you own in that company? 20
##How much does each share cost? 49584
##What is the new sell price? 51943
##What is the commission? 0.02
##
##Stock Name:  Tenisballs inc.
##Amount paid for the stock:  $      991680.00
##Commission paid on the purchase:  $       19833.60
##Amount the stock sold for:  $     1038860.00
##Commission paid on the sale:  $       20777.20
##Profit(or loss if negative):  $        6569.20
##
##Enter stock name: Razor
##How many shares do you own in that company? 493
##How much does each share cost? 2033
##What is the new sell price? 2045
##What is the commission? 0.01
##
##Stock Name:  Razor
##Amount paid for the stock:  $     1002269.00
##Commission paid on the purchase:  $       10022.69
##Amount the stock sold for:  $     1008185.00
##Commission paid on the sale:  $       10081.85
##Profit(or loss if negative):  $      -14188.54
##
##>>> 
##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW2_PS3_gharios_a.py ====
##How many stocks do you want to enter? 3
##Enter stock name: Chapsticks
##How many shares do you own in that company? 12933
##How much does each share cost? 27127
##What is the new sell price? 282822
##What is the commission? 0.01
##
##Stock Name:  Chapsticks
##Amount paid for the stock:  $   350833491.00
##Commission paid on the purchase:  $     3508334.91
##Amount the stock sold for:  $  3657736926.00
##Commission paid on the sale:  $    36577369.26
##Profit(or loss if negative):  $  3266817730.83
##
##Enter stock name: Tesla
##How many shares do you own in that company? 203
##How much does each share cost? 23994
##What is the new sell price? 24300
##What is the commission? 0.01
##
##Stock Name:  Tesla
##Amount paid for the stock:  $     4870782.00
##Commission paid on the purchase:  $       48707.82
##Amount the stock sold for:  $     4932900.00
##Commission paid on the sale:  $       49329.00
##Profit(or loss if negative):  $      -35918.82
##
##Enter stock name: SpaceX
##How many shares do you own in that company? 29
##How much does each share cost? 22394
##What is the new sell price? 24995
##What is the commission? 0.01
##
##Stock Name:  SpaceX
##Amount paid for the stock:  $      649426.00
##Commission paid on the purchase:  $        6494.26
##Amount the stock sold for:  $      724855.00
##Commission paid on the sale:  $        7248.55
##Profit(or loss if negative):  $       61686.19
##
##>>> 
##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW2_PS3_gharios_a.py ====
##How many stocks do you want to enter? 1
##Enter stock name: NBA
##How many shares do you own in that company? 139
##How much does each share cost? 2349
##What is the new sell price? 1930
##What is the commission? 0.05
##
##Stock Name:  NBA
##Amount paid for the stock:  $      326511.00
##Commission paid on the purchase:  $       16325.55
##Amount the stock sold for:  $      268270.00
##Commission paid on the sale:  $       13413.50
##Profit(or loss if negative):  $      -87980.05
##
##>>> 
##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW2_PS3_gharios_a.py ====
##How many stocks do you want to enter? 2
##Enter stock name: Steam
##How many shares do you own in that company? 500
##How much does each share cost? 43
##What is the new sell price? 58
##What is the commission? 0.1
##
##Stock Name:  Steam
##Amount paid for the stock:  $       21500.00
##Commission paid on the purchase:  $        2150.00
##Amount the stock sold for:  $       29000.00
##Commission paid on the sale:  $        2900.00
##Profit(or loss if negative):  $        2450.00
##
##Enter stock name: Google
##How many shares do you own in that company? 2
##How much does each share cost? 102394
##What is the new sell price? 203495
##What is the commission? 0.2
##
##Stock Name:  Google
##Amount paid for the stock:  $      204788.00
##Commission paid on the purchase:  $       40957.60
##Amount the stock sold for:  $      406990.00
##Commission paid on the sale:  $       81398.00
##Profit(or loss if negative):  $       79846.40
##
##>>> 
