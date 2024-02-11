#Andrew Gharios
#Student ID: 1149366
#HW3, PS2: Write a program to check whether a string entered is a palindrome.

def isPalindrome(word):
    '''This function figures out if the word inputed is a palindrome'''
    low = 0
    high = len(word)-1

    while low < high:
        if word[low] != word[high]:        #checking every single character in the input until all have been checked
            return False 
        low += 1        #Moving a character up and down from both sides
        high -= 1
    return True
  


def main():
    '''main function to call isPalindrome and get input from user and then print output'''
    n = int(input("How many words do you want to check? "))
    for i in range(n):
        word = input("Enter a String: ")
        if isPalindrome(word):
            print(word, "is a palindrome")
        else:
            print(word, "is not a palindrome")

if __name__ == "__main__":
    main()

##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 3\HW 3-1.py =========
##How many words do you want to check? 3
##Enter a String: noon
##noon is a palindrome
##Enter a String: test
##test is not a palindrome
##Enter a String: poland
##poland is not a palindrome
##>>> 
##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 3\HW 3-1.py =========
##How many words do you want to check? 3
##Enter a String: dad
##dad is a palindrome
##Enter a String: son
##son is not a palindrome
##Enter a String: roll
##roll is not a palindrome
##>>> 
##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 3\HW 3-1.py =========
##How many words do you want to check? 1
##Enter a String: oh
##oh is not a palindrome
##>>> 
##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 3\HW 3-1.py =========
##How many words do you want to check? 4
##Enter a String: no
##no is not a palindrome
##Enter a String: civic
##civic is a palindrome
##Enter a String: lead
##lead is not a palindrome
##Enter a String: paper
##paper is not a palindrome
##>>> 
##========== RESTART: C:\Users\smgne\Desktop\Python CS 10\HW 3\HW 3-1.py =========
##How many words do you want to check? 2
##Enter a String: racecar
##racecar is a palindrome
##Enter a String: level
##level is a palindrome
>>> 
