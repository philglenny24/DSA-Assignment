def single_number(nums):
    result = 0
    for num in nums:
        result ^= num 
    return result

# Example Test Cases
nums1 = [2, 2, 1]
print(single_number(nums1))  # Output: 1

nums2 = [4, 1, 2, 1, 2]
print(single_number(nums2))  # Output: 4