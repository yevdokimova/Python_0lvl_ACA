def insertion_sort(nums):
    for i in range(len(nums)):
        value_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > value_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j+1] = value_to_insert
    return nums


numbers = [int(num) for num in input('Please input a numbers: ').split()]
print(insertion_sort(numbers))
