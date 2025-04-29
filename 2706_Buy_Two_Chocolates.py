class Solution(object):
    def buyChoco(self, prices, money):
        og=sorted(prices)
        for i in range(0,len(og)-1,2):  # minus 1 to prevent index out of range
            if money >= og[i] + og[i + 1]:
                money -= og[i] + og[i + 1]
                return money
        return money
sol=Solution()
price=[69,91,78,19,40,13]
print(sol.buyChoco(price,94))
        