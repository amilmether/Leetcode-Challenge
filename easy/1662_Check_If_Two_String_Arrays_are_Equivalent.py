class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        return ''.join(word1) == ''.join(word2)

sol=Solution()
arr1=["ab", "c"]
arr2=["a", "bc"]
print(sol.arrayStringsAreEqual(arr1,arr2))