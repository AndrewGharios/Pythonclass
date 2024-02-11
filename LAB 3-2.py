def show_interest(principal:float,rate:float,periods:float):
    '''function interest calculates interest and prints it with the correct format'''
    interest = principal * rate * periods
    print("The interest is: $", format(interest, ',.2f'))

def main():
    '''main function that calls for show_interest and plugs in the wanted numbers'''
    show_interest(rate = 0.01,periods = 10,principal = 10000) #given rates

if __name__ == '__main__':
    print("The simplest interest will be: $1,000.00")
    main()
    
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-2.py ========
##The simplest interest will be: $1,000.00
##The interest is: $ 1,000.00
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-2.py ========
##The simplest interest will be: $1,000.00
##The interest is: $ 1,000.00
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-2.py ========
##The simplest interest will be: $1,000.00
##The interest is: $ 1,000.00
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-2.py ========
##The simplest interest will be: $1,000.00
##The interest is: $ 1,000.00
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-2.py ========
##The simplest interest will be: $1,000.00
##The interest is: $ 1,000.00
##>>> 
