class Solution(object):
    def sortedSquares(self, nums):
        result=[]
        for num in nums:
            result.append(num*num)
        return sorted(result)
sol=Solution()
print(sol.sortedSquares([-7,-3,2,3,11]))