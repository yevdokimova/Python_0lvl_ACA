user_input = list(input('Please input a word: '))

input_rev = user_input[::-1]

if user_input == input_rev:
    print('Yes')
else:
    print('No')
