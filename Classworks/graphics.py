def draw_arrow(num, *, symbol='* '):
    for i in range(1, num + 1):
        print(symbol * i)

    for i in range(num - 1):
        print(symbol * (num - i - 1))


number = int(input('Enter a number: '))

draw_arrow(number, symbol='// ')

# Solution 2

# i = 1
# increment = 1
#
# while i != 0:
#     print("* " * i)
#     if i == n:
#         increment = -1
#     i += increment
