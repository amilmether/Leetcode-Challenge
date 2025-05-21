class Solution(object):
    def plusOne(self, digits):
        stri=''.join(map(str,digits))
        new= int(stri)+1
        return [int(d) for d in str(new)]
sol=Solution()
arr=[1,2,3]
print(sol.plusOne(arr))