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
#Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#lenght : Print the number of items in the tuple:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Tuple Items - Data Types : Tuple items can be of any data type:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#The tuple() Constructor : It is also possible to use the tuple() constructor to make a tuple.: Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
# Access Tuple Items:Print the second item in the tuple:You can access tuple items by referring to the index number, inside square brackets:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#Range of Indexes:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

#Change Tuple Values Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
"""
Using Asterisk*:
If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

Example
Add a list of values the "tropic" variable:
"""

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
"""
Join Two Tuples
To join two or more tuples you can use the + operator:

Get your own Python Server
Join two tuples:
"""

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

