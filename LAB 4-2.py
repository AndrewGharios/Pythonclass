def makeList()->list:
    '''This function creates a list and appends nubers into it.'''
    origlist = []
    for i in range(1,11):
        origlist.append(i)
    return origlist

def delEven(origlist:list):
    '''This function deletes all even numbers from appended list.'''
    x = 0
    while x < len(origlist):
        if origlist[x] % 2 == 0:
            del origlist[x]
            x -= 1
        x += 1
    

def main():
    numlist = makeList()
    print("Original list: ", str(numlist))
    delEven(numlist)
    print("List after deleting even numbers: ", str(numlist))

if __name__ == "__main__":
    main()


##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-2.py ========
##Original list:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##List after deleting even numbers:  [1, 3, 5, 7, 9]
##>>>
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-2.py ========
##Original list:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##List after deleting even numbers:  [1, 3, 5, 7, 9]
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-2.py ========
##Original list:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##List after deleting even numbers:  [1, 3, 5, 7, 9]
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-2.py ========
##Original list:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##List after deleting even numbers:  [1, 3, 5, 7, 9]
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-2.py ========
##Original list:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##List after deleting even numbers:  [1, 3, 5, 7, 9]
##>>> 
