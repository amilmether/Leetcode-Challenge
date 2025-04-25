class Solution(object):
    def checkPerfectNumber(self, num):
        perfect_num=[6,28,496,8128,33550336]
        return num in perfect_num
    
sol= Solution()
print(sol.checkPerfectNumber(28))
        