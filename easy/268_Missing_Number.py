class Solution(object):
    def missingNumber(self, nums):
        return sum(range(0,len(nums)+1))-sum(nums)

sol=Solution()
arr=[0,1]
print(sol.missingNumber(arr))