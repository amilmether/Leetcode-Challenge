from collections import Counter
class Solution(object):
    def judgeCircle(self, moves):
        c = Counter(moves)
        return c['U'] == c['D'] and c['L'] == c['R']


sol=Solution()
print(sol.judgeCircle("UD"))