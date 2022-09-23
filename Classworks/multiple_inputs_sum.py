numbers = [int(elem) for elem in input('Please input a numbers: ').split()]

if len(numbers) == 1:
    print(numbers[0])
else:
    for elem in numbers:
        elem += elem
    print(elem)

