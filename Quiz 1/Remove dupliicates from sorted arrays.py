def remove_duplicates(nums):
    if not nums:
        return 0
    
    unique_index = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]
    return unique_index + 1

# Example Test Cases
nums1 = [1, 1, 2]
print(remove_duplicates(nums1))  # Output: 2

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(remove_duplicates(nums2))  # Output: 5