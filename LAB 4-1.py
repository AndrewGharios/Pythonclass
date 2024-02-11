def main():
    country = input("Enter the name of the country: ")
    Countrycheck(country)
    


def Countrycheck(country):
    BRICS = ["Brazil","Russia","India","China","Sri Lanka"]
    if country in BRICS:
        print(country, "is a member of BRICS")
    else:
        print(country, "is not a member of BRICS")
        

if __name__ == "__main__":
    main()

##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB 4/LAB 4-1.py ========
##Enter the name of the country: Brazil
##Brazil is a member of BRICS
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB 4/LAB 4-1.py ========
##Enter the name of the country: Russia
##Russia is a member of BRICS
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB 4/LAB 4-1.py ========
##Enter the name of the country: USA
##USA is not a member of BRICS
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB 4/LAB 4-1.py ========
##Enter the name of the country: Poland
##Poland is not a member of BRICS
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB 4/LAB 4-1.py ========
##Enter the name of the country: Sri Lanka
##Sri Lanka is a member of BRICS
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB 4/LAB 4-1.py ========
##Enter the name of the country: China
##China is a member of BRICS
##>>> 
