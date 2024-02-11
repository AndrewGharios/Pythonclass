def readValues()->list:
    '''This function takes inputs from user and puts them in a list'''
    looper = 0
    lst = []
    while looper < 1:
        userinp = input("Please enter values, Q to quit: ")
        words = userinp.split()
        for word in words:
            if word == "Q":
                looper = 99
                return lst
            else:
                lst.append(float(word))


def findLargest(lst:list)->(float):
    '''This function finds the largest value in given list'''
    biggest = 0
    for x in lst:
        if x > biggest:
            biggest = x
    return biggest

def display(numbers):
    '''This function prints out the list of inputs and marks the biggest value with an arrow'''
    biggest = findLargest(numbers)
    print("Here are the numbers in the list:")
    for num in numbers:
        print(num, end='')
        if num == biggest:
            print("<== This is the largest number")
        else:
            print()
def main():
    display(readValues())


if __name__ == "__main__":
    main()
    
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-5.py ========
##Please enter values, Q to quit: 3
##Please enter values, Q to quit: 52
##Please enter values, Q to quit: 2.5
##Please enter values, Q to quit: 63.6
##Please enter values, Q to quit: 99.9
##Please enter values, Q to quit: Q
##Here are the numbers in the list:
##3.0
##52.0
##2.5
##63.6
##99.9<== This is the largest number
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-5.py ========
##Please enter values, Q to quit: 58
##Please enter values, Q to quit: 69.99
##Please enter values, Q to quit: 5
##Please enter values, Q to quit: 312
##Please enter values, Q to quit: 56.4
##Please enter values, Q to quit: 33
##Please enter values, Q to quit: Q
##Here are the numbers in the list:
##58.0
##69.99
##5.0
##312.0<== This is the largest number
##56.4
##33.0
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-5.py ========
##Please enter values, Q to quit: 49
##Please enter values, Q to quit: 28
##Please enter values, Q to quit: 512
##Please enter values, Q to quit: 567.67
##Please enter values, Q to quit: 584.65
##Please enter values, Q to quit: 90.0
##Please enter values, Q to quit: 33
##Please enter values, Q to quit: Q
##Here are the numbers in the list:
##49.0
##28.0
##512.0
##567.67
##584.65<== This is the largest number
##90.0
##33.0
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-5.py ========
##Please enter values, Q to quit: 666
##Please enter values, Q to quit: 32
##Please enter values, Q to quit: 5.5
##Please enter values, Q to quit: 39.9
##Please enter values, Q to quit: 3.21
##Please enter values, Q to quit: 2
##Please enter values, Q to quit: Q
##Here are the numbers in the list:
##666.0<== This is the largest number
##32.0
##5.5
##39.9
##3.21
##2.0
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-5.py ========
##Please enter values, Q to quit: 97
##Please enter values, Q to quit: 24
##Please enter values, Q to quit: 62
##Please enter values, Q to quit: 1.2
##Please enter values, Q to quit: 5.322
##Please enter values, Q to quit: 74.78
##Please enter values, Q to quit: 3.56
##Please enter values, Q to quit: 63.36
##Please enter values, Q to quit: Q
##Here are the numbers in the list:
##97.0<== This is the largest number
##24.0
##62.0
##1.2
##5.322
##74.78
##3.56
##63.36
##>>>  
    
