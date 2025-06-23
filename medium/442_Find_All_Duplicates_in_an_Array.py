class Solution(object):
    def findDuplicates(self, nums):
        res = []
        for n in nums:
            n=abs(n)
            if nums[n - 1]<0:
                res.append(n)
            nums[n - 1] = -nums[n-1]
        return res
        