class Solution(object):
    def buyChoco(self, prices, money):
        sort=sorted(prices)
        n=len(prices)
        if n <= 1:
            return money
        amount = sort[0] + sort[1]
        if amount > money:
            return money
        else:
            return money - amount
sol=Solution()
price=[69,91,78,19,40,13]
print(sol.buyChoco(price,94))
        