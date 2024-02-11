#my way
num = float(input("Enter a number: "))
biggest = 0   #this could be an input by the user rather than 0 if needed(changes might apply under)

while num != -999:
    if biggest < num:
        biggest = num
    num = float(input("Input another number or enter -999 to end: "))

print("The biggest number you entered was: ", format(biggest, ",.2f"))
      
#Teacher's way

