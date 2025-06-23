class Solution(object):
    def fib(self,n):
        a=0
        b=1
        if n==2:
            return 1
        for i in range(1,n):
            c=a+b
            a=b
            b=c
        return c
sol=Solution()
print(sol.fib(2))