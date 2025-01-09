#In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False#
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# Evaluate Values and Variables : The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello"))
print(bool(15))

#Most Values are True : The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
