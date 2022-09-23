def has_symbol(values, symbol):
    for char in values:
        if char not in symbol:
            continue
        return True


def is_password_valid(password):
    is_valid = False

    symbols = ['abcdefjhijklmnopqrstuvwxyz', 'abcdefjhijklmnopqrstuvwxyz'.capitalize(), '1234567890', '#$@']

    for symbol in symbols:
        if not has_symbol(password, symbol):
            return is_valid

    return 6 <= len(password) <= 16


if is_password_valid(input('Input a password: ')):
    print('Yes')
else:
    print('No')
