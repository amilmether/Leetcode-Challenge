class Solution(object):
    def alternateDigitSum(self, n):
        finl=0
        iw=1
        for i in str(n) :
            if iw % 2 == 0:
                finl -= int(i) 
                iw+=1
            else:
                finl += int(i)
                iw+=1
        return finl
sol=Solution()
print(sol.alternateDigitSum(886996))