def getData():
    '''Length and Height of a given triangle via user input'''
    length = float(input("Enter the length of a triangle: "))        #inputs by user
    ph = float(input("Enter the perpendicular height of a triangle: "))
    return length , ph


def trigArea(length, ph)->(float):
    '''calculate the area of the triangle returns it'''     
    area = 0.5 * length * ph       #given calculations
    return area


def DisplayData(length,ph,area):
    '''Output with all data from above'''
    print("length of a triangle: ",length)
    print("Perpendicular height of a triangle: ",ph)
    print("area of the triangle: ",area)

def main():
    '''main function to call functions in sequence and define variables'''
    length,ph = getData()
    area = trigArea(length,ph)
    DisplayData(length,ph,area)



if __name__ == "__main__":
    main()

##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-3.py ========
##Enter the length of a triangle: 10
##Enter the perpendicular height of a triangle: 43
##length of a triangle:  10.0
##Perpendicular height of a triangle:  43.0
##area of the triangle:  215.0
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-3.py ========
##Enter the length of a triangle: 11
##Enter the perpendicular height of a triangle: 2.3
##length of a triangle:  11.0
##Perpendicular height of a triangle:  2.3
##area of the triangle:  12.649999999999999
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-3.py ========
##Enter the length of a triangle: 49.5
##Enter the perpendicular height of a triangle: 34.3
##length of a triangle:  49.5
##Perpendicular height of a triangle:  34.3
##area of the triangle:  848.925
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-3.py ========
##Enter the length of a triangle: 23.12
##Enter the perpendicular height of a triangle: 4.3
##length of a triangle:  23.12
##Perpendicular height of a triangle:  4.3
##area of the triangle:  49.708
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-3.py ========
##Enter the length of a triangle: 0.2
##Enter the perpendicular height of a triangle: 0.2
##length of a triangle:  0.2
##Perpendicular height of a triangle:  0.2
##area of the triangle:  0.020000000000000004
##>>> 
    
