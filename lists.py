names = ['bob', 'john', 'sarah', 'alex', 'steven']
print(names)
print(names[1:])
print(names[:])
print(names[1:4])
print(names[1:5])

 #finding largest number in a list
numbers = [323423,6123124,24124123,3512344,213413,956433234534,5464,45672,1324342,68895,85643345345]
max = numbers[0]
for number in numbers:
    if number > max:
        max=number
print(max)