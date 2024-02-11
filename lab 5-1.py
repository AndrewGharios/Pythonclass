dict = {"A": 8, "D": 3, "B": 15, "F": 2, "C": 6}
print(dict.keys())
print(dict.values())

for keys, values in dict.items():
    print(keys, values)
print("In key order: ")
sortedlist = sorted(dict.items())

for keys, values in sortedlist:
    print(keys, values)
total = 0
avg = 0

for keys, values in sortedlist:
    avg = avg + values
    total = total + 1
print("Average is: \n", avg / total)
str=""


##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB5/lab 5-1.py =========
##dict_keys(['A', 'D', 'B', 'F', 'C'])
##dict_values([8, 3, 15, 2, 6])
##A 8
##D 3
##B 15
##F 2
##C 6
##In key order: 
##A 8
##B 15
##C 6
##D 3
##F 2
##Average is: 
## 6.8
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB5/lab 5-1.py =========
##dict_keys(['A', 'D', 'B', 'F', 'C'])
##dict_values([8, 3, 15, 2, 6])
##A 8
##D 3
##B 15
##F 2
##C 6
##In key order: 
##A 8
##B 15
##C 6
##D 3
##F 2
##Average is: 
## 6.8
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB5/lab 5-1.py =========
##dict_keys(['A', 'D', 'B', 'F', 'C'])
##dict_values([8, 3, 15, 2, 6])
##A 8
##D 3
##B 15
##F 2
##C 6
##In key order: 
##A 8
##B 15
##C 6
##D 3
##F 2
##Average is: 
## 6.8
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB5/lab 5-1.py =========
##dict_keys(['A', 'D', 'B', 'F', 'C'])
##dict_values([8, 3, 15, 2, 6])
##A 8
##D 3
##B 15
##F 2
##C 6
##In key order: 
##A 8
##B 15
##C 6
##D 3
##F 2
##Average is: 
## 6.8
##>>> 
##========= RESTART: C:/Users/smgne/Desktop/Python CS 10/LAB5/lab 5-1.py =========
##dict_keys(['A', 'D', 'B', 'F', 'C'])
##dict_values([8, 3, 15, 2, 6])
##A 8
##D 3
##B 15
##F 2
##C 6
##In key order: 
##A 8
##B 15
##C 6
##D 3
##F 2
##Average is: 
## 6.8
##>>> 
