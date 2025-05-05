class Solution(object):
    def countNegatives(self, grid):
        count=0
        for i in grid:
            for j in i:
                if j<0:
                    count+=1
        return count
    
sol=Solution()
arr=[[3,2],[1,0]]
print(sol.countNegatives(arr))
        