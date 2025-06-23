class Solution(object):
    def differenceOfSum(self, nums):
        sum=0
        sum2=0
        for num in nums:
            sum+=num
            while num>0:
                sum2+=num%10
                num =num//10
        return sum - sum2

sol=Solution()
arry=[1,15,6,3]
print(sol.differenceOfSum(arry))
        
