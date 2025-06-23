class Solution(object):
    def furthestDistanceFromOrigin(self, s:str)-> int:
        return abs(s.count('L') - s.count('R')) + s.count('_')

sol=Solution()
print(sol.furthestDistanceFromOrigin("L_RL__R"))