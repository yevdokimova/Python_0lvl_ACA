def selection_sort(nums):
    for i in range(len(nums)):
        min_num_ind = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_num_ind]:
                min_num_ind = j
        nums[i], nums[min_num_ind] = nums[min_num_ind], nums[i]

    return nums


numbers = [int(num) for num in input('Please input a numbers: ').split()]
print(selection_sort(numbers))
