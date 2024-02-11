#Andrew Gharios
#Student ID: 1149366
#HW 3, Set 3: This program inputs a credit card number and checks for availability. 

def main():
    numbercredits = int(input("How many credit cards are you entering? "))
    for i in range(numbercredits):  #for loop to allow user prompt number of credit cards they wanna enter.
        number = input("Enter a credit number: ")
        if isValid(number):  #checking if card is valid or not.
            print("credit card number is valid")
        else:
            print("credit card number is not valid")


def isValid(number):
    '''This checks if the credit number is valid or not'''
    if (sumOfOddPlace(number)+sumOfDoubleEvenPlace(number))%10 == 0:
        return True
    else:
        return False


def sumOfOddPlace(number):
    '''This function calculates the sum of odd numbers.'''
    total = 0
    c = 1
    for i in range(len(number)-1,-1,-1): #reverse loop
        if c%2 == 0: #odd number check
            total += int(number[i])
            c += 1
    return total


def sumOfDoubleEvenPlace(number):
    total = 0
    c = 1
    for i in range(len(number)-1,-1,-1):
        if c%2 != 0: #even number check
            val = int(number[i])*2
        if val >= 10: #if val is greater than 10 or equal to 10 then it's a double digit value
            total += getDigit(str(val)) #convert val into string
            c +=1
        else:
            total += val
            c += 1
    return total


def getDigit(number):
    val = int(number[0])+ int(number[1]) #sum of two digits by using string format
    return val

if __name__=="__main__":
    main()


##==== RESTART: C:/Users/smgne/Desktop/Python CS 10/HW 3/HW3_PS3_Gharios_A.py ====
##How many credit cards are you entering? 3
##Enter a credit number: 4388576018410707
##credit card number is not valid
##Enter a credit number: 5345445036331908
##credit card number is valid
##Enter a credit number: 4539674610066890
##credit card number is not valid
##>>> 
##==== RESTART: C:/Users/smgne/Desktop/Python CS 10/HW 3/HW3_PS3_Gharios_A.py ====
##How many credit cards are you entering? 2
##Enter a credit number: 374386396429012
##credit card number is valid
##Enter a credit number: 375710484435319
##credit card number is not valid
##>>> 
##==== RESTART: C:/Users/smgne/Desktop/Python CS 10/HW 3/HW3_PS3_Gharios_A.py ====
##How many credit cards are you entering? 2
##Enter a credit number: 5511672836006764
##credit card number is not valid
##Enter a credit number: 5418749264807295
##credit card number is valid
##>>>  
##==== RESTART: C:/Users/smgne/Desktop/Python CS 10/HW 3/HW3_PS3_Gharios_A.py ====
##How many credit cards are you entering? 3
##Enter a credit number: 6011003441082300
##credit card number is valid
##Enter a credit number: 6011491451654276
##credit card number is not valid
##Enter a credit number: 6011200176787281
##credit card number is valid
##>>>
##==== RESTART: C:/Users/smgne/Desktop/Python CS 10/HW 3/HW3_PS3_Gharios_A.py ====
##How many credit cards are you entering? 5
##Enter a credit number: 5574729507844610
##credit card number is valid
##Enter a credit number: 5574729507844610
##credit card number is valid
##Enter a credit number: 6011296080751751
##credit card number is not valid
##Enter a credit number: 6011387532677288
##credit card number is valid
##Enter a credit number: 349921340267167
##credit card number is not valid
##>>>


