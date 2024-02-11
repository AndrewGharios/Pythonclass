def are_anagrams(word1:str,word2:str):
    '''this function determines if inputed words are anagrams'''
    list_word1 = list(word1)
    list_word1.sort()      #turn word1 into a list and sort it into array alphabetical order
    list_word2 = list(word2)
    list_word2.sort()

    if list_word1 == list_word2:
        print("The words", word1 ,"and", word2 ,"are anagrams.")
    else:
        print("The words", word1 ,"and", word2 ,"aren't anagrams.")


def main():
    '''acquired user input and called function are_anagrams to check for anagrams'''
    valid_input_bool = False
    while not valid_input_bool:
        try:
            two_words = input("Enter two space seperated words: ")
            word1,word2 = two_words.split()  #splitting the inputs into a list of words
            are_anagrams(word1,word2) #calling are_anagrams
            valid_input_bool = True
        except ValueError:
            print("Bad Input")
    

if __name__ == "__main__":
    main()

##
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-6.py ========
##Enter two space seperated words: silent listen
##The words silent and listen are anagrams.
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-6.py ========
##Enter two space seperated words: dad
##Bad Input
##Enter two space seperated words: dad bad sad
##Bad Input
##Enter two space seperated words: sad dad
##The words sad and dad aren't anagrams.
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-6.py ========
##Enter two space seperated words: iceman cinema
##The words iceman and cinema are anagrams.
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-6.py ========
##Enter two space seperated words: python thonpy
##The words python and thonpy are anagrams.
##>>> 
##========= RESTART: C:\Users\smgne\Desktop\Python CS 10\LAB 4\LAB 4-6.py ========
##Enter two space seperated words: freddy andy
##The words freddy and andy aren't anagrams.
##>>> 
