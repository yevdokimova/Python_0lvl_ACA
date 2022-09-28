# Solution 1

def check_ascending(values):
    for i in range(len(values) - 2):
        if values[i] >= values[i + 1]:
            return False
    return True


def check_descending(values):
    for i in range(len(values) - 2):
        if values[i] <= values[i + 1]:
            return False
    return True


def check_monotonicity(values):

    if check_ascending(values):
        return "Ascending"
    elif check_descending(values):
        return "Descending"
    else:
        return "Neither"
#
#
# Soltuion 2

# def check_monotonicity(values):
#
#     is_ascending = True
#     is_descending = True
#
#     for i in range(len(values) - 1):
#         if is_descending and values[i] <= values[i + 1]:
#             is_descending = False
#         if is_ascending and values[i] >= values[i + 1]:
#             is_ascending = False
#
#     if is_ascending:
#         return "Ascending"
#     if is_descending:
#         return "Descending"
#     else:
#         return "Neither"


numbers = [int(num) for num in input('Please input a numbers: ').split()]
print(check_monotonicity(numbers))
