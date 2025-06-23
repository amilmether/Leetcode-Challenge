import re
class Solution(object):
    def isPalindrome(self, s):
        result=re.sub(r"[^a-z0-9]","",s.lower())
        return result == result[::-1]
            