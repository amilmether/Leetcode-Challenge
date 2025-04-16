class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        new=[]
        for i in range(0,len(nums),2):#2 is the step up value like i+2
            new.append(nums[i+1])
            new.append(nums[i])
        return new
sol=Solution()
nums=[5,4,2,3]
print(sol.numberGame(nums))