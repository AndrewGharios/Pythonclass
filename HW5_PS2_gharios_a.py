#Andrew Gharios
#Student ID: 1449366
#HW 5, PS2: Program where the user enters an abbreviation and the program translates the abbreviation. 

textabbv = dict() #Create a dictionary
file = open('textabbv.txt')#open file
for line in file:
    line = line.strip()       #strip and split line
    fields = line.split(':')
    if len(fields) == 2:                  #if list contains 2= add new entry
        textabbv[fields[0]] = fields[1]
file.close() #closing file

while True:
    userinput = input('Enter a message to be translated: ') #user input with abbreviation
    if userinput == 'exit': #sentinel to exit loop
        break
    words = userinput.split(' ')                   #Punctuation character (not include the first and last) occure in the text
    output = ''                               #Loop through each word                                     
    for i in words:
        if i.lower() in textabbv: #converting input to lowercase and checking if its in the dictionary
            output += textabbv[i]
        else:
            output += i
        output += ' ' #appending a space
    print('The translated text is:')
    print(output)
 
 


##Enter a message to be translated: y r u sad
##The translated text is:
##why are you sad 
##
##Enter a message to be translated: pls nter the room
##The translated text is:
##pls enter the room 
##
##Enter a message to be translated: np wuts the problem rofl
##The translated text is:
##no problem what's the problem rolling on floor laughing 
##
##Enter a message to be translated: fyi its my bday
##The translated text is:
##for your information its my birthday 
##
##Enter a message to be translated: Thor aka God of Thunder 
##The translated text is:
##Thor also known as God of Thunder   
