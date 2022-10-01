def missing_numbers(nums):
    n = len(nums) + 1

    for i in range(1, n + 1):
        if i not in nums:
            return i


numbers = [int(i) for i in input('Enter a numbers: ').split()]
print(missing_numbers(numbers))
