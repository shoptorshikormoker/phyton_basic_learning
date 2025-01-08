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