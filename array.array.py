import array

a = array.array('i', [0, 0, 0, 0, 0])

# access the element at index 2
print(a[2])

# modify the element at index 2
a[2] = 10
print(a[2])

# YOU CAN ALSO APPEND ELEMENTS AT THE END OF THE ARRAY
a.append(20)
print(a)        # Output:  array('i', [0, 0, 10, 0, 0, 20])

# if you need to add an element in a different possition, do:
a.insert(0, 30)     
print(a)        # Output: array('i', [30, 0, 0, 10, 0, 0, 20])

# ---------------------------------------------------------------------

# Create an array of integers
a = array.array('i', [10, 20, 30, 40, 50])

# Remove and return the last elemnt form the array
last = a.pop()
print(last)     # 50
print(a)        # array('i', [10, 20, 30, 40])

# Remove and return the element at index 2
middle = a.pop(2)
print(middle)   # 30
print(a)        # array('i', [10, 20, 40])

