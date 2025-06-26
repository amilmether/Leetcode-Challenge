# 205. Isomorphic Strings [Easy]
# Tags: misc

class Solution:
    def isIsomorphic(self, s, t):
        mapping = dict()
        for i in range(len(s)):
            if s[i] not in mapping:
                if t[i] in mapping.values():
                    return False
                mapping[s[i]] = t[i]
            elif mapping[s[i]] != t[i]:
                return False
        return True