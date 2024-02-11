def get_sales()->float:
    sales=float(input("Enter the monthly sales: "))   # Input the amount of sales
    return sales


def get_advanced_pay()->float:  # Get the amount of advanced pay through input.
    print("Enter the amount of advanced pay, or \nenter 0 if no advanced pay was given.")
    advanced_pay=float(input("Advanced pay:"))
    return advanced_pay

def determine_comm_rate(sales:float)->float:
    if sales < 10000.00:        #sales with calculated rates.
        rate = 0.10
    elif sales >= 10000.00 and sales <= 14999.99:
        rate = 0.12
    elif sales >= 15000.00 and sales <= 17999.99:
        rate = 0.14
    elif sales >= 18000.00 and sales <= 21999.99:
        rate = 0.16
    elif sales > 21999.99:
        rate = 0.18

    return rate

def main():
    sales = get_sales()
    advanced_pay = get_advanced_pay()
    comm_rate = determine_comm_rate(sales)
    pay = sales * comm_rate - advanced_pay
    print('The pay is $', format(pay, ',.2f'), sep='') # Display the amount of pay.
    if pay < 0: #making sure no negative numbers
        print('The salesperson must reimburse the company.')


if __name__=="__main__":
    main()


##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-4.py ========
##Enter the monthly sales: 239324
##Enter the amount of advanced pay, or 
##enter 0 if no advanced pay was given.
##Advanced pay:233
##The pay is $42,845.32
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-4.py ========
##Enter the monthly sales: 1500
##Enter the amount of advanced pay, or 
##enter 0 if no advanced pay was given.
##Advanced pay:0
##The pay is $150.00
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-4.py ========
##Enter the monthly sales: 3844
##Enter the amount of advanced pay, or 
##enter 0 if no advanced pay was given.
##Advanced pay:300
##The pay is $84.40
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-4.py ========
##Enter the monthly sales: 1920
##Enter the amount of advanced pay, or 
##enter 0 if no advanced pay was given.
##Advanced pay:30
##The pay is $162.00
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-4.py ========
##Enter the monthly sales: 20
##Enter the amount of advanced pay, or 
##enter 0 if no advanced pay was given.
##Advanced pay:48555
##The pay is $-48,553.00
##The salesperson must reimburse the company.
##>>> 
