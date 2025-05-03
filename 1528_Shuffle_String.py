class Solution(object):
    def restoreString(self, s, indices):
            result=[''] * len(s)
            for i,idx in enumerate(indices):
                result[idx]=s[i]
            return ''.join(result)

sol=Solution()
str="codeleet"
ind=[4,5,6,7,0,2,1,3]
print(sol.restoreString(str,ind))