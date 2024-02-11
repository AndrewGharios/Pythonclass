def createList()->(list):
    '''this function creates a list and appends user inputed list'''
    userinput = input("Enter a list of numbers: ")
    lst = userinput.split(",")
    return lst


def removeDuplicates(lst:list)->(list):
    '''this function removes all duplicates in inputed list'''
    newlist = []
    for x in lst:
        if x not in newlist:
            newlist.append(x)
    return newlist
    
       
def main():
    lst = createList()
    print("Original list: ", lst)
    lst = removeDuplicates(lst)
    print("List after removing duplicates: ", lst)


if __name__ == "__main__":
    main()

##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-3.py ========
##Enter a list of numbers: 1,5,6,2,5,7,1
##Original list:  ['1', '5', '6', '2', '5', '7', '1']
##List after removing duplicates:  ['1', '5', '6', '2', '7']
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-3.py ========
##Enter a list of numbers: 5,7,8,1,2,4,5,2,1,5,6,9
##Original list:  ['5', '7', '8', '1', '2', '4', '5', '2', '1', '5', '6', '9']
##List after removing duplicates:  ['5', '7', '8', '1', '2', '4', '6', '9']
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-3.py ========
##Enter a list of numbers: 4,6,7,1,1,1,4
##Original list:  ['4', '6', '7', '1', '1', '1', '4']
##List after removing duplicates:  ['4', '6', '7', '1']
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-3.py ========
##Enter a list of numbers: 4,4,4,4,4,1,2,4,5
##Original list:  ['4', '4', '4', '4', '4', '1', '2', '4', '5']
##List after removing duplicates:  ['4', '1', '2', '5']
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-3.py ========
##Enter a list of numbers: 5,6,1,22,56,8,52
##Original list:  ['5', '6', '1', '22', '56', '8', '52']
##List after removing duplicates:  ['5', '6', '1', '22', '56', '8', '52']
##>>> 
