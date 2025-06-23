class Solution(object):
    def toLowerCase(self, s):
        final=[]
        for c in s:
            if 'A' <= c <= 'Z':
                final.append(chr(ord(c) + 32))
            else:
                final.append(c)
        return ''.join(final)
sol=Solution()
print(sol.toLowerCase("HELLO"))