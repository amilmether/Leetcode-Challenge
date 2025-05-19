class Solution(object):
    def firstPalindrome(self, words):
        for word in words:
            if word == word[::-1]:
                return word
        return ""
sol=Solution()
arr=["abc","car","ada","racecar","cool"]
print(sol.firstPalindrome(arr))