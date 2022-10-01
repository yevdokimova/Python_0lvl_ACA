def largest_number(n):
    is_largest = True

    for i in range(len(n) - 1):
        if n[i + 1] > n[i]:
            is_largest = False

    return is_largest


if largest_number(input('Enter a numbers: ')):
    print('Yes')
else:
    print('No')


