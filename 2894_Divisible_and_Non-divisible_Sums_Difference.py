class Solution(object):
    def differenceOfSums(self, n, m):
        if m == 0:
            return 0
        for i in range(1,n+1):
            if i % m == 0:
                num2+=i
            else:
                num1+=i
        return num1-num2
sol=Solution()
print(sol.differenceOfSums(1,0))
