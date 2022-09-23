def odd_numbers(start, stop):
    odd_numbers = []
    for elem in range(start, stop):
        if is_odd(elem):
            odd_numbers.append(elem)

    return odd_numbers


def is_odd(number):

    for i in str(number):
        if int(i) % 2 == 0:
            return False
    return True


num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print(odd_numbers(num1, num2))
