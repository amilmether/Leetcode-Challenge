class Solution(object):
    def countEven(self, num):
        def countsum(n):
            return sum(map(int , str(n)))
        return sum(1 for i in range(1,num+1) if countsum(i)%2 == 0)
sol=Solution()
print(sol.countEven(30))