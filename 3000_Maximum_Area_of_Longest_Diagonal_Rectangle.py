class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
       best = 0
       area = 0
       for L,W in dimensions:
        d = L * L + W * W
        if d > best:
            best = d
            ans = L * W
        elif d == best:
            ans = max( ans, L * W )
       return ans
sol=Solution()
arr=[[9,3],[8,6]]
print(sol.areaOfMaxDiagonal(arr))



        