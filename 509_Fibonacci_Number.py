class Solution(object):
    def fib(self,n):
        a=0
        b=1 
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a = b
            b = c
            print(c)
sol=Solution()
print(sol.fib(10))