class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        new=[]
        for a,b in zip(nums[::2],nums[1::2]):#2 is the step up value like i+2
            new.append(b)
            new.append(a)
        return new
sol=Solution()
nums=[5,4,2,3]
print(sol.numberGame(nums))