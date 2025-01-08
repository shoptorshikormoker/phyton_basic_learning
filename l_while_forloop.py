# Using a while loop to sum numbers
num = 5
total = 0
while num > 0:
    total += num
    num -= 1
print("Sum using while:", total)

# Using a for loop to sum numbers
total = 0
for num in range(1, 6):
    total += num
print("Sum using for:", total)
# Print numbers from 0 to 4
for i in range(5):
    print(i)

# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# Print numbers from 1 to 10 with a step of 2
for i in range(1, 11, 2):
    print(i)