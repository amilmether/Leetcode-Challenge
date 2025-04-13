class Solution(object):
    def findGCD(self, nums):
        small=large=nums[0]
        for num in nums:
            if num < small:
                small = num
            if num > large:
                large = num
        if small == large :
            return small
        while large!= 0:
            small,large=large,small%large 
        a=small
        return a
sol=Solution()
arr=[2,5,6,9,10]
print(sol.findGCD(arr))

        