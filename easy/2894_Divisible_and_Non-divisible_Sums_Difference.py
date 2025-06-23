class Solution(object):
    def differenceOfSums(self, n, m):
        sum=n*(n+1) // 2
        div=n//m
        sum_div=m * div * (div+1) // 2
        return sum - 2*sum_div
sol=Solution()
print(sol.differenceOfSums(10,3))
