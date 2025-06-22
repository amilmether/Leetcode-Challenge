class Solution(object):
    def sortSentence(self, s):
        words=s.split()
        sorted_words = sorted(words, key=lambda word: int(re.search(r'\d+$', word).group()))
        num_removed_words=[re.sub(r'\d+$', '', word) for word in sorted_words]
        return ' '.join(num_removed_words)
