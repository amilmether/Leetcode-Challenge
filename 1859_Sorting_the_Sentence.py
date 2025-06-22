class Solution(object):
    def sortSentence(self, s):
        words = s.split()
        sorted_words = [''] * len(words)

        for word in words:
            index = int(word[-1]) -1
            sorted_words[index] = word[:-1]
        
        return ' '.join(sorted_words)   