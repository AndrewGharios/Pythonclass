#-Write a program to calculate the average of 3
#Test scores. Grading as follows: 
#Average 90 or greater A
#             80 to 89 B
#             70 to 79 C
#             69 to below F



#input
print()
print("Input your test scores below")
test1 = int(input("Test 1:"))
test2 = int(input("Test 2:"))
test3 = int(input("Test 3:"))
avg = (test1 + test2 + test3)/ 3

#processing:
##if 90 <= avg <= 100:  
##    print("A")
##
##if 80 <= avg <= 89:
##    print("B")
##
##if 70 <=avg <= 79:
##    print("C")
##
##if 0 <= avg <= 69:
##    print("F")
##    
##if avg > 100:
##    
##    print("out of range")
##    
##if avg < 0:
##    print("LMAO what")


#Programmer's/Better way to program above ^:        #Refer to Truth Table:
if avg >= 90 and avg <= 100:                        #T and T = T , T and F = F etc..
    print("A")
if avg >= 80 and avg <=89:
    print("B")
if avg >= 70 and avg <=79:
    print("C")
if avg >= 0 and avg <=69:
    print("F")
