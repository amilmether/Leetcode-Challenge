from collections import Counter
class Solution(object):
    def checkIfPangram(self, sentence):
        count=Counter(sentence)
        if len(count) == 26:
            return True
        return False
