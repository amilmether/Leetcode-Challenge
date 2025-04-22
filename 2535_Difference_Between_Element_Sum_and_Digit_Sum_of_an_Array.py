class Solution(object):
    def differenceOfSum(self, nums):
        sum1=''.join(map(str, nums))
        sum4=int(sum1)
        sum2=sum(nums)
        sum3=0
        while sum4 > 0:
            sum3+= sum4 % 10
            sum4 = sum4 // 10
        return sum2 - sum3
sol=Solution()
arry=[1,15,6,3]
print(sol.differenceOfSum(arry))
        
