class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        sumof=sum(map(int,str(x)))
        return sumof if x % sumof == 0 else -1

sol=Solution()
print(sol.sumOfTheDigitsOfHarshadNumber(18))
        