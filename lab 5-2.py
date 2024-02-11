def main():
    '''main function to take an input of a year and determine its rank by calling the function'''
    years = int(input("Enter the year: "))
    print(determineRank(years))  

def determineRank(years):
    '''This function determines which rank is the inputted year'''
    dict = {1:"Infant", 2:"Child", 3:"Adult", 4:"Senior" }
    return dict[years]

if __name__ == "__main__":
    main()
##
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB5/lab 5-2.py =========
##Enter the year: 2
##Child
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB5/lab 5-2.py =========
##Enter the year: 3
##Adult
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB5/lab 5-2.py =========
##Enter the year: 1
##Infant
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB5/lab 5-2.py =========
##Enter the year: 4
##Senior
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB5/lab 5-2.py =========
##Enter the year: 3
##Adult
##>>> 
