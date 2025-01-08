#Tuple items can be of any data type
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
my_tuple = (10, 20, 30, 40, 50)

# Accessing elements
print(my_tuple[0])   # Output: 10
print(my_tuple[-1])  # Output: 50

# Slicing
print(my_tuple[1:4])  # Output: (20, 30, 40)
tuple1 = (1, 2, 3)
print(len(tuple1))  # Output: 3