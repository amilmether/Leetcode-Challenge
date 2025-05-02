class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        if ''.join(word1) == ''.join(word2):
            return True
        else:
            return False

sol=Solution()
arr1=["ab", "c"]
arr2=["a", "bc"]
print(sol.arrayStringsAreEqual(arr1,arr2))