"""
1.Rules for Python variables name:
2.Python Variable Naming Rules:
3.Start with a letter or _ (not a digit).
4.Use only letters, digits, and _ (no spaces or special characters).
5.Case-sensitive (name ≠ Name).
6.Avoid reserved keywords (e.g., if, class).
7.Use meaningful names; avoid overwriting built-in functions (e.g., print).
"""
x = 5
y = "Hello, World!"
print(x)
print(y)

# Single or Double Quotes?: String variables can be declared either by using single or double quotes:

x = "John"
# is the same as
x = 'John'

#Case-Sensitive: Variable names are case-sensitive
a = 4
A = "Sally"
print(a,A)
#A will not overwrite a

#Camel Case : Each word, except the first, starts with a capital letter:

myVariableName = "John"

#Snake Case: Each word is separated by an underscore character:

my_variable_name = "John"

#One Value to Multiple Variables: And you can assign the same value to multiple variables in one line:

x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection: If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output Variables : The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)

#gobel variable : Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)