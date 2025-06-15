class Solution(object):
    def isAnagram(self, s, t):
        count={}
        count1={}
        for word1,word2 in zip(s,t):
            count[word1] = count.get(word1,0)+1
            count1[word2] = count1.get(word2,0)+1
        if count == count1:
            return True
        return False
sol=Solution()        
print(sol.isAnagram("rat","car"))
        