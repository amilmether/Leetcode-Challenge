class Solution(object):
    def mostWordsFound(self, sentences):
        max_words=0
        for words in sentences:
            word_count= len(words.split())
            max_words=max(max_words,word_count)
        return max_words 
    
sol=Solution()
arr=["please wait", "continue to fight", "continue to win"]
print(sol.mostWordsFound(arr))