def swapFirstLast(list_integers:list)->(list):
    '''this function swaps the first and last element in the list'''
    tempr = list_integers[0]
    list_integers [0] = list_integers[len(list_integers)-1]
    list_integers[len(list_integers)-1] = tempr
    return list_integers

def shiftRight(list_integers:list)->(list):
    '''this funtion moves all values in the list to the right and the last one to the front'''
    newlist = []
    newlist.append(list_integers[len(list_integers)-1])
    for x in range(0,len(list_integers)-1):
        newlist.append(list_integers[x])
    return newlist

def replaceEven(list_integers:list)->(list):
    '''This function replaces all even values in the list to 0'''
    for x in range(1,len(list_integers)):
        if (list_integers[x] % 2) == 0:
            list_integers[x] = 0
    return list_integers

def replaceNeighbors(list_integers:list)->(list):
    '''this function replaces the last and first value by its two neighbours'''
    for x in range(1,len(list_integers)-1):
        larger = list_integers[x - 1]
        if larger < list_integers[x + 1]:
            larger = list_integers[x + 1]
        list_integers[x] = larger
    return list_integers

def removeMiddle(list_integers:list)->(list):
    '''this function removes the middle element if the list is odd, or the middle two elements if even'''
    firstMiddle = int((len(list_integers) / 2) -1)
    newInts = []
    for x in range(0,firstMiddle):
        newInts.append(list_integers[x])
    if (len(list_integers) % 2 == 0):
        for x in range(firstMiddle,len(list_integers)-2):
            newInts.append(list_integers[x + 1 ])
    return newInts

def evenToFront(list_integers:list)->(list):
    '''This function moves all even values to the front'''
    Even = 0
    for x in range(0,len(list_integers)):
        if (list_integers[x] % 2) == 0:
            tempr = list_integers[x]
            list_integers[x] = list_integers[Even]
            list_integers[Even] = tempr
            Even += 1
    return list_integers

def secondLargest(list_integers:list)->(float):
    "This function returns the second largest element in inputed list"
    list_integers.sort()
    secondlargest = list_integers[len(list_integers) - 2]
    return secondlargest

    
def isIncreasing(list_integers:list):
    '''This function returns true if the input list is in increasing order and sorted'''
    element = list_integers[0]
    for x in range(1,len(list_integers)):
        if element > list_integers[x]:
            return False
        element = list_integers[x]
    return True

def hasAdjacentDuplicate(list_integers:list):
    '''If the inputed list has two adjacent elements, function returns True'''
    for x in range(0,len(list_integers)):
        if list_integers[x] == list_integers[x - 1]:
            return True
    return False


def hasDuplicate(list_integers:list):
    '''This function returns True if list contain duplicates'''
    for x in range(0,len(list_integers)):
        for i in range(0,len(list_integers)):
            if (x != i and list_integers[x] == list_integers[i]):
                return True
    return False

def main():
    '''main function to call all functions and print outputs'''
    list_integers = [11,42,66,78,45,16,3,5,94,2]

    print("The original data for all functions is: ", list_integers)
    
    data = list(list_integers)
    swapFirstLast(data)
    print("After swapping first and last: ", data)

    data = list(list_integers)
    shiftRight(data)
    print("After shifting right: ", data)

    data = list(list_integers)
    replaceEven(data)
    print("After replacing even elements: ", data)

    data = list(list_integers)
    replaceNeighbors(data)
    print("After replacing with neighbors: ", data)

    data = list(list_integers)
    removeMiddle(data)
    print("After removing the middle element(s): ", data)

    data = list(list_integers)
    evenToFront(data)
    print("After moving even elements: ", data)

    
    print("The second largest value is: ", secondLargest(list_integers))
    print("The list is in increasing order: ", isIncreasing(list_integers))
    print("The list has adjacent duplicates: ", hasAdjacentDuplicate(list_integers))
    print("The list has duplicates: ", hasDuplicate(list_integers))


if __name__ == "__main__":
    main()


##>>>
##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 4\hw4-1.py ==========
##The original data for all functions is:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##After swapping first and last:  [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
##After shifting right:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##After replacing even elements:  [1, 0, 3, 0, 5, 0, 7, 0, 9, 0]
##After replacing with neighbors:  [1, 3, 4, 5, 6, 7, 8, 9, 10, 10]
##After removing the middle element(s):  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##After moving even elements:  [2, 4, 6, 8, 10, 3, 7, 1, 9, 5]
##The second largest value is:  9
##The list is in increasing order:  True
##The list has adjacent duplicates:  False
##The list has duplicates:  False
##>>> 
##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 4\hw4-1.py ==========
##The original data for all functions is:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##After swapping first and last:  [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
##After shifting right:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##After replacing even elements:  [1, 0, 3, 0, 5, 0, 7, 0, 9, 0]
##After replacing with neighbors:  [1, 3, 4, 5, 6, 7, 8, 9, 10, 10]
##After removing the middle element(s):  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##After moving even elements:  [2, 4, 6, 8, 10, 3, 7, 1, 9, 5]
##The second largest value is:  9
##The list is in increasing order:  True
##The list has adjacent duplicates:  False
##The list has duplicates:  False
##>>> 
##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 4\hw4-1.py ==========
##The original data for all functions is:  [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]
##After swapping first and last:  [103, 20, 10, 14, 54, 16, 75, 38, 79, 12]
##After shifting right:  [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]
##After replacing even elements:  [12, 0, 0, 0, 0, 0, 75, 0, 79, 103]
##After replacing with neighbors:  [12, 12, 14, 54, 54, 75, 75, 79, 103, 103]
##After removing the middle element(s):  [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]
##After moving even elements:  [12, 20, 10, 14, 54, 16, 38, 75, 79, 103]
##The second largest value is:  79
##The list is in increasing order:  True
##The list has adjacent duplicates:  False
##The list has duplicates:  False
##>>> 
##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 4\hw4-1.py ==========
##The original data for all functions is:  [42, 5, 8, 20, 45, 3, 21, 16, 24, 2]
##After swapping first and last:  [2, 5, 8, 20, 45, 3, 21, 16, 24, 42]
##After shifting right:  [42, 5, 8, 20, 45, 3, 21, 16, 24, 2]
##After replacing even elements:  [42, 5, 0, 0, 45, 3, 21, 0, 0, 0]
##After replacing with neighbors:  [42, 42, 42, 45, 45, 45, 45, 45, 45, 2]
##After removing the middle element(s):  [42, 5, 8, 20, 45, 3, 21, 16, 24, 2]
##After moving even elements:  [42, 8, 20, 16, 24, 2, 21, 5, 45, 3]
##The second largest value is:  42
##The list is in increasing order:  True
##The list has adjacent duplicates:  False
##The list has duplicates:  False
##>>> 
##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 4\hw4-1.py ==========
##The original data for all functions is:  [4, 56, 79, 2, 5, 43, 10, 56, 1, 75]
##After swapping first and last:  [75, 56, 79, 2, 5, 43, 10, 56, 1, 4]
##After shifting right:  [4, 56, 79, 2, 5, 43, 10, 56, 1, 75]
##After replacing even elements:  [4, 0, 79, 0, 5, 43, 0, 0, 1, 75]
##After replacing with neighbors:  [4, 79, 79, 79, 79, 79, 79, 79, 79, 75]
##After removing the middle element(s):  [4, 56, 79, 2, 5, 43, 10, 56, 1, 75]
##After moving even elements:  [4, 56, 2, 10, 56, 43, 79, 5, 1, 75]
##The second largest value is:  75
##The list is in increasing order:  True
##The list has adjacent duplicates:  True
##The list has duplicates:  True
##>>> 
##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 4\hw4-1.py ==========
##The original data for all functions is:  [11, 42, 66, 78, 45, 16, 3, 5, 94, 2]
##After swapping first and last:  [2, 42, 66, 78, 45, 16, 3, 5, 94, 11]
##After shifting right:  [11, 42, 66, 78, 45, 16, 3, 5, 94, 2]
##After replacing even elements:  [11, 0, 0, 0, 45, 0, 3, 5, 0, 0]
##After replacing with neighbors:  [11, 66, 78, 78, 78, 78, 78, 94, 94, 2]
##After removing the middle element(s):  [11, 42, 66, 78, 45, 16, 3, 5, 94, 2]
##After moving even elements:  [42, 66, 78, 16, 94, 2, 3, 5, 45, 11]
##The second largest value is:  78
##The list is in increasing order:  True
##The list has adjacent duplicates:  False
##The list has duplicates:  False
##>>> 
