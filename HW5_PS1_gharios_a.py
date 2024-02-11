#Andrew Gharios
#Student ID: 1449366
#Homework 5, PS 1: This program reads tea.txt and print it's report

file = open("tea.txt","r") #opening the file
Dict={}              # Create an empty dictionary
for line in file:            
    line=line.strip('\n')   #Stripping end-of-line characters at the end of each line
    line=line.split(':',1)     
    Dict[line[0]] = line[1:]

store1_sum=store2_sum=store3_sum=0  
col_width =15
  
for key in sorted(Dict):
    valuelist=Dict[key]
    valuelist=str(valuelist[0])
    valuelist=valuelist.split(':')    #splitting the values so that we get 3 stores or 3 values 
    valuelist_sum=0
    store1_sum+=float(valuelist[0])
    store2_sum+=float(valuelist[1])
    store3_sum+=float(valuelist[2])  
    for i in valuelist:               
        valuelist_sum = valuelist_sum + float(i)
    output=[str(key),str(valuelist[0]),str(valuelist[1]),str(valuelist[2]),str(valuelist_sum)]   # Print the key and it's values and sum of values
    print("".join(value.ljust(col_width) for value in output))

output=["",format(store1_sum, ',.2f'),format(store2_sum,',.2f'),format(store3_sum, ',.2f')]
print("".join(value.ljust(col_width) for value in output))
file.close()          #closing the file


##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/HW 5/PS1 HW5.py =========
##Ceylon         6700.1         5012.45        6011.0         17723.55       
##Earl Grey      10225.25       9025.0         9505.0         28755.25       
##Green Tea      8580.0         7201.25        8900.0         24681.25       
##Jasmine        9285.15        8276.1         8705.0         26266.25       
##Mint Tea       7901.25        4267.0         7056.5         19224.75       
##               42,691.75      33,781.80      40,177.50      
##>>> 

