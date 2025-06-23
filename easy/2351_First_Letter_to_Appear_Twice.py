class Solution(object):
    def repeatedCharacter(self, s):
        count={}
        for word in s:
            count[word] = count.get(word,0)+1
            if count[word] == 2:
                return word
        