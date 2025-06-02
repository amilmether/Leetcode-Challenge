class Solution(object):
    def isAcronym(self, words, s):
        if len(words) != len(s):
            return False
        
        for words,s in zip(words,s):
            if s not in words[0]:
                return False
        return True


sol=Solution()
print(sol.isAcronym(["alice","bob","charlie"],"ab"))
        