class Solution(object):
    def hammingWeight(self, n):
        return bin(n).count('1')
    
sol=Solution()
print(sol.hammingWeight(11))