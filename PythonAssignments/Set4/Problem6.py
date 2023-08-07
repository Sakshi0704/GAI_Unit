def missing_number(nums):
    n = len(nums)
    total_sum = (n * (n + 1)) // 2
    array_sum = sum(nums)
    return total_sum - array_sum


input_array = [1,3,5]
result = missing_number(input_array)
print(result) 