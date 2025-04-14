class Solution(object):
    def defangIPaddr(self, address):
        array=[]
        for i in address:
            if i == '.':
                array.append("[.]")
            else:
                array.append(i)
        ip_address = ''.join(array)
        return ip_address

sol=Solution()
print(sol.defangIPaddr("123.45.67.89"))