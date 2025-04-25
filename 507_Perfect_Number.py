class Solution(object):
    def checkPerfectNumber(self, num):
        sum=0
        for i in range(1,num):
            if num % i == 0:
                sum+=i
            if sum==num:
                return True
        return False
    
sol= Solution()
print(sol.checkPerfectNumber(7))
        