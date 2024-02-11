#Sudent Name: Andrew Gharios
#Student ID: 1149366
#This program makes a grocery store bill with amount, tax and discount quantities included.

#user input
sold_qty = float(input("How many items were sold? "))
value = float(input("How much does each item cost? "))         #Amount of products sold to be inputed by user, including taxes and discounts.
discount = float(input("What is the discount amount in %: "))
tax = float(input("What is the tax amount ? "))

#calculations:
amount = sold_qty * value                                  
discount_amount = amount * discount / 100                        #calculations for total amount to be payed.
subtotal = amount - discount_amount
tax_amount = subtotal * tax/100
total_amount = subtotal + tax_amount

#output                                                                                        #Bill output with spacers to make it partly allign.
print()
print("***********BILL***********")
print("Quantity sold:\t\t\t\t", sold_qty)
print("Price per item:\t\t\t\t", value)
print("\t\t\t\t    ---------------")
print("Amount:\t\t\t\t\t",format(amount,',.2f'))
print("Discount:\t\t\t       -", format(discount, ',.2f'))
print("\t\t\t\t    ---------------")
print("Discounted Total:\t\t\t",format(discount_amount, ',.2f'))
print("Tax:\t\t\t\t       +",format(tax_amount,',.2f'))
print("\t\t\t\t    ---------------")
print("Total amount to be paid:\t\t$",format(total_amount, ',.2f'))


##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/bill program.py =========
##How many items were sold? 123
##How much does each item cost? 324.22
##What is the discount amount in %: 20
##What is the tax amount ? 10
##
##***********BILL***********
##Quantity sold:				 123.0
##Price per item:				 324.22
##				    ---------------
##Amount:					 39,879.06
##Discount:			       - 20.00
##				    ---------------
##Discounted Total:			 7,975.81
##Tax:				       + 3,190.32
##				    ---------------
##Total amount to be paid:		$ 35,093.57
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/bill program.py =========
##How many items were sold? 49
##How much does each item cost? 46
##What is the discount amount in %: 5.5
##What is the tax amount ? 10
##
##***********BILL***********
##Quantity sold:				 49.0
##Price per item:				 46.0
##				    ---------------
##Amount:					 2,254.00
##Discount:			       - 5.50
##				    ---------------
##Discounted Total:			 123.97
##Tax:				       + 213.00
##				    ---------------
##Total amount to be paid:		$ 2,343.03
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/bill program.py =========
##How many items were sold? 74
##How much does each item cost? 293.45
##What is the discount amount in %: 15
##What is the tax amount ? 9.3
##
##***********BILL***********
##Quantity sold:				 74.0
##Price per item:				 293.45
##				    ---------------
##Amount:					 21,715.30
##Discount:			       - 15.00
##				    ---------------
##Discounted Total:			 3,257.30
##Tax:				       + 1,716.59
##				    ---------------
##Total amount to be paid:		$ 20,174.60
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/bill program.py =========
##How many items were sold? 58
##How much does each item cost? 93.5
##What is the discount amount in %: 30
##What is the tax amount ? 48
##
##***********BILL***********
##Quantity sold:				 58.0
##Price per item:				 93.5
##				    ---------------
##Amount:					 5,423.00
##Discount:			       - 30.00
##				    ---------------
##Discounted Total:			 1,626.90
##Tax:				       + 1,822.13
##				    ---------------
##Total amount to be paid:		$ 5,618.23
##>>>
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/bill program.py =========
##How many items were sold? 74
##How much does each item cost? 248
##What is the discount amount in %: 10
##What is the tax amount ? 76
##
##***********BILL***********
##Quantity sold:				 74.0
##Price per item:				 248.0
##				    ---------------
##Amount:					 18,352.00
##Discount:			       - 10.00
##				    ---------------
##Discounted Total:			 1,835.20
##Tax:				       + 12,552.77
##				    ---------------
##Total amount to be paid:		$ 29,069.57
##>>> 
