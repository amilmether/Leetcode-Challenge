class Solution(object):
    def isPerfectSquare(self, num):
        return True if (num ** 0.5).is_integer() else False
        

sol=Solution()
print(sol.isPerfectSquare(16))