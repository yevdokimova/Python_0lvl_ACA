def is_largest(n):
    _is_largest = True

    while n > 9:
        digit_right = n % 10
        digit_left = n // 10 % 10

        if digit_right > digit_left:
            _is_largest = False
            break

        n //= 10

    return _is_largest


if is_largest(int(input('Enter a numbers: '))):
    print('Yes')
else:
    print('No')
