class Solution(object):
    def countEven(self, num):
        total=0
        count=0
        for i in range(1,num+1):
            while i > 0:
                total+=i%10
                i=i//10
            if total % 2 == 0:
                count+=1
            total=0
        return count
sol=Solution()
print(sol.countEven(30))