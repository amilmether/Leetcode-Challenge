class Solution(object):
    def missingNumber(self, nums):
        for i in range(0,len(nums)+1):
            if i in nums:
                pass
            else:
                return i

sol=Solution()
arr=[9,6,4,2,3,5,7,0,1]
print(sol.missingNumber(arr))