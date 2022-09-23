user_num = int(input("Please enter the number: "))


def factorial(num):
    fact = 1
    i = 1
    while i <= num:
        if num == 0:
            fact = 1
            break
        fact = fact * i
        i += 1
    return fact


print(factorial(user_num))
