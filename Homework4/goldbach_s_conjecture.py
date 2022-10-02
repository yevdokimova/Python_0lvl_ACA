def is_prime(num):
    _is_prime = True

    if num <= 1:
        _is_prime = False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            _is_prime = False
            break

    return _is_prime


def goldbach_s_conjecture(num):
    for i in range(2, num - 2 + 1):
        if is_prime(i) and is_prime(num - i):
            return i, num - i


print(goldbach_s_conjecture(int(input('Enter a number: '))))
