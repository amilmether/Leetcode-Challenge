class Solution(object):
    def twoSum(self, nums, target):
        hashmap={}
        for i,n in enumerate(nums):
            diff= target - n
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[n] = i
        return
        
sol=Solution()
arry=[10, 22, 5, 75, 65, 80, 30, 110, 90, 150, 120, 50, 70, 40]
tar=130
print(sol.twoSum(arry,tar))