user_input = input('Please enter the text you want to check: ')


def is_palindrome(text):
    str_len = len(text)
    if str_len == 1:
        return True
    for i in range(0, str_len // 2):
        if text[i] != text[len(text) - i - 1]:
            return False
    return True


if is_palindrome(user_input):
    print("Yes")
else:
    print("No")
