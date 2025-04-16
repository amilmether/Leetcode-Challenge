class Solution(object):
    def numberGame(self, nums):
        new = []
        while nums:
            alice = min(nums)
            nums.remove(alice)
            bob = min(nums)
            nums.remove(bob)
            new.append(bob)
            new.append(alice)
        return new
        
sol=Solution()
nums=[5,4,2,3]
print(sol.numberGame(nums))