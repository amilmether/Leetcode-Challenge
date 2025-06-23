class Solution(object):
    def climbStairs(self, n):
        if n <= 3:
            return n
        a=0
        b=1
        n+=1
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        return c
sol=Solution()
print(sol.climbStairs(5))
