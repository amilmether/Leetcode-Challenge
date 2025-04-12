class Solution(object):
    def commonFactors(self, a,b):
        while b != 0:
            a,b=b,a%b
        gcd = a
        cf =[] 
        for i in range(1, gcd +1):
            if (a % i == 0):
                cf.append(i)
        return cf


sol=Solution()
print(sol.commonFactors(100,80))