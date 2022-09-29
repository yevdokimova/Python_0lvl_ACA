def merge(l1, l2):
    lst = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            lst.append(l1[i])
            i += 1
        else:
            lst.append(l2[j])
            j += 1

    lst.extend(l1[i:] + l2[j:])

    return lst


def merge_sort(numbers, start, end):
    if start == end - 1:
        return numbers[start:end]
    mid = (start + end) // 2
    return merge(merge_sort(numbers, start, mid), merge_sort(numbers, mid, end))


