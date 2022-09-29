def reverse_print(n):
    if not n:
        return
    num = int(input('Enter a number: '))
    reverse_print(n-1)
    print(num)
