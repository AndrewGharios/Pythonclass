#Initialization
sum = 0
count = 0



#input
num = int(input("Input your number, or enter -999 to quit: "))

while num != -999:
    sum = sum + num
    count = count + 1
    num = int(input("Input another number, or enter -999 to quit: "))

if count != 0:
    avg = sum/count
    print("Your sum is: ", sum)
    print("Your Average is: ",format(avg, ".2f"))
    print("quitting...")


    





