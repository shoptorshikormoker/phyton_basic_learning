my_set = {1, 2, 3}
my_set.add(4)  # Adds 4 to the set
print(my_set)  # Output: {1, 2, 3, 4}
my_set = {1, 2, 3}
my_set.clear()  # Removes all elements
print(my_set)   # Output: set()
my_set = {1, 2, 3}
print(2 in my_set)   # Output: True
print(4 in my_set)   # Output: False
my_set = {1, 2}
my_set.add(3)          # Adds a single element
my_set.update({4, 5})  # Adds multiple elements
print(my_set)          # Output: {1, 2, 3, 4, 5}