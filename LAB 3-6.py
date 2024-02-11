def string_total(number):
    '''This function calculates the sum of every single digit in an inputed number'''
    total = 0
    while( number > 0):                      #making sure every number inputed is not 0)
        total += number % 10  
        number = number // 10
    return total                            #return statement

def main():
    '''This is the main fuction, it prints the inputed number by the user, then calls for string_total to calculate the number'''
    number = int(input("Enter a sequence of digits with nothing separating them: "))
    print("The total of the digits in the string you entered is", string_total(number))

if __name__ == "__main__":
    main()

##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-6.py ========
##Enter a sequence of digits with nothing separating them: 12371238
##The total of the digits in the string you entered is 27
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-6.py ========
##Enter a sequence of digits with nothing separating them: 4414224
##The total of the digits in the string you entered is 21
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-6.py ========
##Enter a sequence of digits with nothing separating them: 123
##The total of the digits in the string you entered is 6
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-6.py ========
##Enter a sequence of digits with nothing separating them: 4942855
##The total of the digits in the string you entered is 37
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-6.py ========
##Enter a sequence of digits with nothing separating them: 44444444
##The total of the digits in the string you entered is 32
##>>> 
