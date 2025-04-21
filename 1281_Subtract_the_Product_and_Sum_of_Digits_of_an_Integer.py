class Solution(object):
    def subtractProductAndSum(self, n):
        product=1
        total=0
        while n>0:
            total += n % 10
            product *= n % 10
            n = n//10
        return product-total
sol=Solution()
print(sol.subtractProductAndSum(234))