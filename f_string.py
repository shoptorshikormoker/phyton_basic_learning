# Creating strings
string1 = 'Hello'
string2 = "World"

string3 = '''This is
a multi-line string'''

# Accessing characters
print(string1[0])  # output: 'H' (first character)
print(string2[-1]) # output: 'd' (last character)

# Slicing : Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])
"""
negativeindexing

Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])

Negative Indexing
Use negative indexes to start the slice from the end of the string:

Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):
"""
b = "Hello, World!"
print(b[-5:-2])


# Concatenation :To concatenate, or combine, two strings you can use the + operator.

print(string1 + ' ' + string2)  # 'Hello World'

# Repetition
print(string1 * 3)  # 'HelloHelloHello'


# Length
print(len(string1))  # 5

Placeholders and Modifiers: Add a placeholder for the price variable:

price = 59
txt = f"The price is {price} dollars"
print(txt)

Escape characters : To fix this problem, use the escape character \" The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."
print(txt) 