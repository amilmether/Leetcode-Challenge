class Solution(object):
    def findGCD(self, nums):
        small=large=nums[0]
        
        if nums[0] == nums[1]:
            small=large=nums[0]
            return nums[0]
        else:
            for num in nums:
                if num < small:
                    small = num
                if num > large:
                    large = num
        while large!= 0:
            small,large=large,small%large 
        a=small
        return a
sol=Solution()
arr=[2,5,6,9,10]
print(sol.findGCD(arr))

        