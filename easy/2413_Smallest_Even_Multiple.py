class Solution(object):
    def smallestEvenMultiple(self, n):
        if n % 2 !=0 :
            return n * 2
        return n
sol=Solution()
print(sol.smallestEvenMultiple(6))