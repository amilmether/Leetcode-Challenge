class Solution(object):
    def truncateSentence(self, s, k):
        arr=s.split()
        return ' '.join(arr[0:k])

sol=Solution()
arr="What is the solution to this problem"
print(sol.truncateSentence(arr,4))