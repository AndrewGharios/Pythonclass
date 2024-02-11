#Sudent Name: Andrew Gharios
#Student ID: 1149366
#HW 2, Set 4: The goal of this project is to make a fictitious comparison of the federal income. You will ask the user to input their taxable income. Use the income brackets given below to calculate the new and old income tax.

#input
PreviousTax = 0
NextTax = 0
user_income = float(input("Enter your income: "))


#pre-calculations
Prev1 = 9235 * 0.10
Prev2 = (37950 - 9326) * 0.15
Prev2 = (91900 - 37951) * 0.25
Prev2 = (191650 - 91901) * 0.28
Prev2 = (416700 - 191651) * 0.33
Prev2 = (418400 - 416700) * 0.35

#calculations/configuration
while user_income >= 0:
    #prev Taxes
    if user_income <=9592:
        NextTax = user_income * 0.10
    elif user_income >= 9526 and user_income <= 38700:  
        NextTax = 952.6 + ((user_income - 9526) * 0.12)
    elif user_income >= 38701 and user_income <= 82500:
        NextTax = 4453.48 + ((user_income - 38701) * 0.22)
    elif user_income >= 825001 and user_income <= 157500:
        NextTax = 14089.26 + ((user_income - 82501) * 0.24)
    elif user_income >= 157501 and user_income <= 200000:
        NextTax = 32089.02 + ((user_income - 157501) * 0.32)
    elif user_income >= 200001 and user_income <= 500000:
        NextTax = 45688.7 + ((user_income - 200001) * 0.35)
    elif user_income >= 500000:
        NextTax = 150688.35 + ((user_income - 500000) * 0.37)

    #next Taxes
    if user_income <= 9325:
        PreviousTax = user_income * 0.10
    elif user_income >= 9326 and user_income <= 37950:
        PreviousTax = Prev1 + ((user_income - 9326) * 0.15)
    elif user_income >= 37951 and user_income <= 91900:
        PreviousTax = Prev1 + ((user_income - 37951) * 0.15)
    elif user_income >= 91901 and user_income <= 191650:
        PreviousTax = Prev1 + ((user_income - 91901) * 0.15)
    elif user_income >= 191651 and user_income <= 416700:
        PreviousTax = Prev1 + ((user_income - 191651) * 0.15)
    elif user_income >= 416701 and user_income <= 418400:
        PreviousTax = Prev1 + ((user_income - 416701) * 0.15)
    elif user_income >= 418401:
        PreviousTax = Prev1 + ((user_income - 418401) * 0.15)

    #extra calcuations
    TaxDiff = NextTax - PreviousTax  * 100
    TaxPercnt = ((NextTax - PreviousTax) / PreviousTax) * 100


#Output
    print("Income: $", format(user_income,',.2f'))
    print("2017 Tax: $", format(PreviousTax, ',.2f'))
    print("2018 Tax: $", format(NextTax, ',.2f'))
    print("Tax Difference(cents): $", format(TaxDiff, ',.2f'))
    print("Tax %: $", format(TaxPercnt, ',.2f'))

    #sentinel         
    print()
    print()
    user_income = float(input("Enter the income: ")) 


##>>> 
##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW2_PS4_gharios_a.py ====
##Enter your income: 2381234
##Income: $ 2,381,234.00
##2017 Tax: $ 295,348.45
##2018 Tax: $ 846,744.93
##Tax Difference(cents): $ -28,688,100.07
##Tax %: $ 186.69
##
##
##Enter the income: 458212
##Income: $ 458,212.00
##2017 Tax: $ 6,895.15
##2018 Tax: $ 136,062.55
##Tax Difference(cents): $ -553,452.45
##Tax %: $ 1,873.31
##
##
##Enter the income: 858482
##Income: $ 858,482.00
##2017 Tax: $ 66,935.65
##2018 Tax: $ 283,326.69
##Tax Difference(cents): $ -6,410,238.31
##Tax %: $ 323.28
##
##
##Enter the income: -1
##>>> 
##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW2_PS4_gharios_a.py ====
##Enter your income: 57999
##Income: $ 57,999.00
##2017 Tax: $ 3,930.70
##2018 Tax: $ 8,699.04
##Tax Difference(cents): $ -384,370.96
##Tax %: $ 121.31
##
##
##Enter the income: 103942
##Income: $ 103,942.00
##2017 Tax: $ 2,729.65
##2018 Tax: $ 8,699.04
##Tax Difference(cents): $ -264,265.96
##Tax %: $ 218.69
##
##
##Enter the income: 80482
##Income: $ 80,482.00
##2017 Tax: $ 7,303.15
##2018 Tax: $ 13,645.30
##Tax Difference(cents): $ -716,669.70
##Tax %: $ 86.84
##
##
##Enter the income: 93242
##Income: $ 93,242.00
##2017 Tax: $ 1,124.65
##2018 Tax: $ 13,645.30
##Tax Difference(cents): $ -98,819.70
##Tax %: $ 1,113.29
##
##
##Enter the income: -1
##>>> 
##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW2_PS4_gharios_a.py ====
##Enter your income: 37832
##Income: $ 37,832.00
##2017 Tax: $ 5,199.40
##2018 Tax: $ 4,349.32
##Tax Difference(cents): $ -515,590.68
##Tax %: $ -16.35
##
##
##Enter the income: 29344
##Income: $ 29,344.00
##2017 Tax: $ 3,926.20
##2018 Tax: $ 3,330.76
##Tax Difference(cents): $ -389,289.24
##Tax %: $ -15.17
##
##
##Enter the income: 38452
##Income: $ 38,452.00
##2017 Tax: $ 998.65
##2018 Tax: $ 4,423.72
##Tax Difference(cents): $ -95,441.28
##Tax %: $ 342.97
##
##
##Enter the income: -1
##>>> 
##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW2_PS4_gharios_a.py ====
##Enter your income: 48555
##Income: $ 48,555.00
##2017 Tax: $ 2,514.10
##2018 Tax: $ 6,621.36
##Tax Difference(cents): $ -244,788.64
##Tax %: $ 163.37
##
##
##Enter the income: 95445
##Income: $ 95,445.00
##2017 Tax: $ 1,455.10
##2018 Tax: $ 6,621.36
##Tax Difference(cents): $ -138,888.64
##Tax %: $ 355.05
##
##
##Enter the income: 1034555
##Income: $ 1,034,555.00
##2017 Tax: $ 93,346.60
##2018 Tax: $ 348,473.70
##Tax Difference(cents): $ -8,986,186.30
##Tax %: $ 273.31
##
##
##Enter the income: -1
##>>> 
##==== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 2\HW2_PS4_gharios_a.py ====
##Enter your income: 234743
##Income: $ 234,743.00
##2017 Tax: $ 7,387.30
##2018 Tax: $ 57,848.40
##Tax Difference(cents): $ -680,881.60
##Tax %: $ 683.08
##
##
##Enter the income: 294585
##Income: $ 294,585.00
##2017 Tax: $ 16,363.60
##2018 Tax: $ 78,793.10
##Tax Difference(cents): $ -1,557,566.90
##Tax %: $ 381.51
##
##
##Enter the income: 29455
##Income: $ 29,455.00
##2017 Tax: $ 3,942.85
##2018 Tax: $ 3,344.08
##Tax Difference(cents): $ -390,940.92
##Tax %: $ -15.19
##
##
##Enter the income: -1
##>>> 
