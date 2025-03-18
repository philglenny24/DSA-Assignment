def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Example Test Cases
nums1 = [1, 2, 3, 1]
print(contains_duplicate(nums1))  # Output: True

nums2 = [1, 2, 3, 4]
print(contains_duplicate(nums2))  # Output: False