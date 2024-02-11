lot_numb = int(input("Enter the lot number or enter -999 to end: "))
tax_factor = 0.0065




while lot_numb != -999:
    prop_value = float(input("Enter the property value: "))
    prop_tax = prop_value * tax_factor
    print(format(prop_tax, ',.2f'))
    print()
    lot_numb = int(input("Enter a lot number or enter -999 to end: "))

##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 1\lab 1-6.py ========
##Enter the lot number or enter -999 to end: 244
##Enter the property value: 1948.4
##12.66
##
##Enter a lot number or enter -999 to end: 124
##Enter the property value: 944230
##6,137.49
##
##Enter a lot number or enter -999 to end: 100
##Enter the property value: 3452.123
##22.44
##
##Enter a lot number or enter -999 to end: -999
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 1\lab 1-6.py ========
##Enter the lot number or enter -999 to end: 124
##Enter the property value: 95442
##620.37
##
##Enter a lot number or enter -999 to end: 96
##Enter the property value: 1094
##7.11
##
##Enter a lot number or enter -999 to end: -999
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 1\lab 1-6.py ========
##Enter the lot number or enter -999 to end: 7891
##Enter the property value: 52856.50
##343.57
##
##Enter a lot number or enter -999 to end: -999
##>>> 
