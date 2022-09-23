# Write a program that created the following based on input number, e.g. for 3:
# 1
# 1 2
# 1 2 3

num = int(input('Please enter a number: '))

for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
