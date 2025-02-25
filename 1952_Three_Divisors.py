class Solution(object):
    def isThree(self, n):
        count=0
        for m in range(1,n+1):
            if n%m==0:
                count+=1
        if count==3:
            return True
        else:
            return False
sol=Solution()
print(sol.isThree(121))
