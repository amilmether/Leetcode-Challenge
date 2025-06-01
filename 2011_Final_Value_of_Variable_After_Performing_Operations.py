class Solution(object):
    def finalValueAfterOperations(self, operations):
        x=0
        for i in operations:
            if "--" in i:
                x-=1
            if "++" in i:
                x+=1
        return x
sol=Solution()
arr=["X++","++X","--X","X--"]
print(sol.finalValueAfterOperations(arr))
