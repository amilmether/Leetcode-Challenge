class Solution(object):
    def reverseWords(self, s):
        return " ".join(s[::-1].split()[::-1])
sol=Solution()
arr="Let's take LeetCode contest"
print(sol.reverseWords(arr))

        