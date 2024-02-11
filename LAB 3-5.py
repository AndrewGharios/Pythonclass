def getInitials(inp:str)->(str):
    '''This function takes the initial out of the inputed full name'''
    words = inp.split() #split list.
    initials = ""
    for i in range (len(words)):  #For loop to get initial of each word in input.(full, middle,last)
        name = words[i] 
        initials += (name[0] + '.')
    return initials #return statement
    

    

def main():
    inp = input('Enter your full name:') #user inputs name.
    getInitials(inp) #call for function
    print(getInitials(inp)) #print output

if __name__ == "__main__":
    main()

##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-5.py ========
##Enter your full name:Don Leo Cun
##D.L.C.
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-5.py ========
##Enter your full name:Robert Downey Junior
##R.D.J.
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-5.py ========
##Enter your full name:Luke Lucky Luke
##L.L.L.
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-5.py ========
##Enter your full name:Ben Mark Davidson
##B.M.D.
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 3\LAB 3-5.py ========
##Enter your full name:Barrack Obama
##B.O.
##>>> 
