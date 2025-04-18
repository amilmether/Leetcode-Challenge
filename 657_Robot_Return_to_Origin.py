class Solution(object):
    def judgeCircle(self, moves):
        x=y=0
        for i in moves:
            if i == 'U':
                y=y+1
            elif i == 'D':
                y=y-1
            elif i == 'L':
                x=x-1
            elif i == 'R':
                x=x+1
        if x == 0 and y == 0:
            return True
        else:
            return False


sol=Solution()
print(sol.judgeCircle("UD"))