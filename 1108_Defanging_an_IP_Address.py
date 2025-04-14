class Solution(object):
    def defangIPaddr(self, address):
        return address.replace('.','[.]')

sol=Solution()
print(sol.defangIPaddr("123.45.67.89"))