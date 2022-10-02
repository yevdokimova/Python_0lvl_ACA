# tail recursion
def reverse_list_tail(l, _list=[]):
    if not l:
        return _list
    return reverse_list_tail(l[:-1], _list + [l[-1]])

# recursion
# def reverse_list(l):
#     if not l:
#         return []
#     return reverse_list(l[1:]) + [l[0]]
