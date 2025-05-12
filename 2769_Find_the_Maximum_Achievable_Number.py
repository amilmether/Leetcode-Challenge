class Solution(object):
    def theMaximumAchievableX(self, num, t):
        return num + 2 * t
    
sol=Solution()
print(sol.theMaximumAchievableX(4,1))