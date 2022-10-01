def is_prime(num):
    _is_prime = True

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            _is_prime = False
            break

    return _is_prime


num_to_check = int(input('Enter a number: '))
if is_prime(num_to_check):
    print('Yes')
else:
    print('No')
