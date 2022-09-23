user_input = list(input("Please enter ticket's number: "))

sep = (len(user_input) // 2 - 1)
first_half = 0
second_half = 0

i = 0

while i < len(user_input):
    if i <= sep:
        first_half += int(user_input[i])
    else:
        second_half += int(user_input[i])
    i += 1

if first_half == second_half:
    print('Yes')
else:
    print('No')
