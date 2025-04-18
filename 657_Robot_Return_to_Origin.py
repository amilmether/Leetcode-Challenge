from collections import Counter
class Solution(object):
    def judgeCircle(self, moves):
        return moves.count('L') == moves.count('R') and moves.count('D') == moves.count('U')


sol=Solution()
print(sol.judgeCircle("UD"))