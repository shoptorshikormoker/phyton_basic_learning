#list

x = [4,7,10]
x[1] = 15
print("Print list X", x)
x.append(12)
print("Print list X after append", x)
x.sort()
print("Sorted X", x)
x.reverse()
print("Reverse Sorted X", x)
print("popped item", x.pop(0))
x = x + [9,10]
print("after different kind if append", x)
#Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#List Items - Data Types:String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
"""
The list() Constructor
It is also possible to use the list() constructor when creating a new list.

Using the list() constructor to make a List:
"""

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
"""
Access Items
List items are indexed and you can access them by referring to the index number:

ExampleGet your own Python Server
Print the second item of the list:
"""

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
"""

Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.

Example
Return the third, fourth, and fifth item:
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])