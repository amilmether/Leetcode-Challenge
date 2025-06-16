def find_difference(nums1, nums2):
    # Step 1: Convert lists to sets
    set1 = set(nums1)
    set2 = set(nums2)

    # Step 2: Compute difference
    only_in_nums1 = list(set1 - set2)
    only_in_nums2 = list(set2 - set1)

    # Step 3: Return the result
    return [only_in_nums1, only_in_nums2]

# Example 1
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
print(find_difference(nums1, nums2))  # Output: [[1, 3], [4, 6]]

# Example 2
nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]
print(find_difference(nums1, nums2))  # Output: [[3], []]
