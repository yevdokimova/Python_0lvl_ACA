user_input = input('Please enter your ticket number: ')


def is_lucky(ticket):
    first_half = 0
    second_half = 0
    for i in list(ticket[:len(ticket) // 2]):
        first_half = first_half + int(i)
    for i in list(ticket[len(ticket) // 2:]):
        second_half = second_half + int(i)

    if first_half == second_half:
        return True
    else:
        return False


if is_lucky(user_input):
    print("Yes")
else:
    print("No")
