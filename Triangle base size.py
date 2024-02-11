base_size = int(input("Enter the triangle base: "))
for row in range(base_size):
    for col in range(row + 1):
        print("*", end = '')
    print()
for row in range(base_size):
    print("*" , end = '')
    print()
