start = int(input("Input the starting number: "))
end = int(input("Input the ending number: "))

print()
print("Number\tSquare")
print('-' * 16 )
for num in range(start, end +1):
    square = num ** 2
    print(num, '\t', square)
    
