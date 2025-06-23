import itertools
class Solution(object):
    def countNegatives(self, grid):
        count=0
        for item in itertools.chain.from_iterable(grid):
            if item < 0:
                count+=1
        return count
    
sol=Solution()
arr=[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(sol.countNegatives(arr))
        