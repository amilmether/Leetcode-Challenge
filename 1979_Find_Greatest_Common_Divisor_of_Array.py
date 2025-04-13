class Solution(object):
    def findGCD(self, nums):
        small=large=nums[0]
        for num in nums:
            if num < small:
                small = num
            if num > large:
                large = num
        while large!= 0:
            small,large=large,small%large 
        a=small
        com=[]
        for i in range(1,small +1):
            if (a % i == 0):
                com.append(i)
        return len(com)
sol=Solution()
arr=[2,5,6,9,10]
print(sol.findGCD(arr))

ex
        