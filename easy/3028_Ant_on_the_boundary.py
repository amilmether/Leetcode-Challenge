class Solution(object):
    def returnToBoundaryCount(self, nums):
        ant = 0 
        bout = 0 
        for n in nums:
            ant += n
            if ant == 0:
                bout += 1
    
        return bout

solution=Solution()   
nums = [1, -1, 2, -2, 3, -3]
res=solution.returnToBoundaryCount(nums)
print(res)