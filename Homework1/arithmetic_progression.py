first_value = int(input('Please enter the first value of the arithmetic progression: '))
second_value = int(input('Please enter the second value of the arithmetic progression: '))
num = int(input('Please enter nth term: '))

n_value = first_value + (num - 1) * (second_value - first_value)

print(f'[{num}] = {n_value}')
