class Solution(object):
    def singleNumber(self, nums):
        result=0
        for num in nums:
            result^=num
        return result
sol=Solution()
arr=[4,1,2,1,2]
print(sol.singleNumber(arr))
                
        