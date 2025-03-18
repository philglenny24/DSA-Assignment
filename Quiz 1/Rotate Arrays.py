def rotate_array(nums, k):
    n = len(nums)
    k = k % n
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

# Example Test Cases
nums1 = [1, 2, 3, 4, 5, 6, 7]
rotate_array(nums1, 3)
print(nums1)  # Output: [5, 6, 7, 1, 2, 3, 4]

nums2 = [-1, -100, 3, 99]
rotate_array(nums2, 2)
print(nums2)  # Output: [3, 99, -1, -100]