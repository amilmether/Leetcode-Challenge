class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[mid] >= target and len(nums) >= 1:
            return mid + 1
        elif nums[mid] <= target and len(nums) < 1:
            print("me")
            return mid + 1
        return nums[mid]
sol=Solution()
arr=[1,3,5,6]
print(sol.searchInsert(arr,0))
