class Solution(object):
    def mostWordsFound(self, sentences):
        top=0
        final=[]
        for words in sentences:
            for word in words.split():
                top+=1
            final.append(top)
            top=0
        return max(final)
    
sol=Solution()
arr=["please wait", "continue to fight", "continue to win"]
print(sol.mostWordsFound(arr))