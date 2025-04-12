class Solution(object):
    def commonFactors(self, a,b):
        cf =[] 
        for i in range(1, max(a,b)+1):
            if (a % i == 0 and b % i == 0):
                cf.append(i)
        return cf


sol=Solution()
print(sol.commonFactors(100,80))