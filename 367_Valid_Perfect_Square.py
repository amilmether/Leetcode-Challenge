class Solution(object):
    def isPerfectSquare(self, num):
        if (num ** 0.5).is_integer():
            return True
        else:
            return False
        

sol=Solution()
print(sol.isPerfectSquare(16))