def digits_sum(num):
    sums = 0
    for elem in num:
        sums += int(elem)
    return sums


def my_root(num):
    root = digits_sum(num)
    while root >= 10:
        root = digits_sum(str(root))
    return root


print(my_root(input('number: ')))
