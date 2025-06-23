class Solution(object):
    def getNoZeroIntegers(self, n):
        x,y= n-1,1
        while "0" in str(y) or "0" in str(x):
            x-=1
            y+=1
        return [x,y]
sol=Solution()
print(sol.getNoZeroIntegers(100))