item_cost = float(input("Enter the item's wholesale cost: "))
repeat = 'y'
counter = 0


while repeat == 'y':
    if counter >= 1:
        item_cost = float(input("Enter the item's wholesale cost: "))
    if item_cost <= 0:
            print("ERROR: the cost cannot be negative")
            item_cost = float(input("Enter the correct wholesale cost: "))
    if item_cost > 0:
        markup = item_cost * 2.5
        print("Retail price is: ", format(markup, ',.2f'))
    counter = 2
    repeat = str(input("Do you have another item?(Enter y for yes): "))


##======== RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 1\lab 1-7 $.py =======
##Enter the item's wholesale cost: 23
##Retail price is:  57.50
##Do you have another item?(Enter y for yes): y
##Enter the item's wholesale cost: 10
##Retail price is:  25.00
##Do you have another item?(Enter y for yes): y
##Enter the item's wholesale cost: 58
##Retail price is:  145.00
##Do you have another item?(Enter y for yes): n
##>>> 
##======== RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 1\lab 1-7 $.py =======
##Enter the item's wholesale cost: 288
##Retail price is:  720.00
##Do you have another item?(Enter y for yes): y
##Enter the item's wholesale cost: 10000
##Retail price is:  25,000.00
##Do you have another item?(Enter y for yes): n
##>>> 
##======== RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 1\lab 1-7 $.py =======
##Enter the item's wholesale cost: 58
##Retail price is:  145.00
##Do you have another item?(Enter y for yes): y
##Enter the item's wholesale cost: -100
##ERROR: the cost cannot be negative
##Enter the correct wholesale cost: 10
##Retail price is:  25.00
##Do you have another item?(Enter y for yes): n
##>>> 
##======== RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 1\lab 1-7 $.py =======
##Enter the item's wholesale cost: 63
##Retail price is:  157.50
##Do you have another item?(Enter y for yes): y
##Enter the item's wholesale cost: 235
##Retail price is:  587.50
##Do you have another item?(Enter y for yes): y
##Enter the item's wholesale cost: 959
##Retail price is:  2,397.50
##Do you have another item?(Enter y for yes): n
##>>> 
