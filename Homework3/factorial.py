def factorial(num):
    i = 1
    result = 1
    while i <= num:
        result *= i
        i += 1

    return result


# solution 2

# def factorial(num):
#     result = 1
#
#     for i in range(2, n+1):
#         result *= 1
#
#     return result


print(factorial(int(input('Enter a number: '))))
