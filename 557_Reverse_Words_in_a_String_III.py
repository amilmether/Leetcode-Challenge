class Solution(object):
    def reverseWords(self, s):
        arr=s.split()
        final=[]
        for arry in arr:
            final.append(arry[::-1])

        return ' '.join(final)
sol=Solution()
arr="Let's take LeetCode contest"
print(sol.reverseWords(arr))

        