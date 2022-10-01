def chairs_sum(heights):
    max_height = max(heights)
    heights_sum = 0

    for elem in heights:
        diff = max_height - elem
        heights_sum += diff

    return heights_sum


nums = [int(i) for i in input('Enter heights of the students: ').split()]
print(chairs_sum(nums))
