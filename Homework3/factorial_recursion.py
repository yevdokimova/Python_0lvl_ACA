def factorial(num):
    if num  == 1 or num == 2:
        return num

    return num * factorial(num - 1)


print(factorial(int(input('Enter a number: '))))