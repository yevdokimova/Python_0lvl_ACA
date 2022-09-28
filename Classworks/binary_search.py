def binary_search(numbers, target, start_ind, end_ind):
    if len(numbers) == 0:
        return False
    mid = (start_ind + end_ind) // 2
    if numbers[mid] == target:
        return True
    if numbers[mid] > target:
        return binary_search(numbers, target, start_ind, mid)  #[start, mid)
    return binary_search(numbers, target, mid+1, end_ind)   #[mid+1, end)

