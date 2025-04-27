class Solution(object):
    def truncateSentence(self, s, k):
        arr=s.split()
        finall=[]
        for i in range(0,k) :
            finall.append(arr[i])
        return ' '.join(finall)
sol=Solution()
arr="Hello how are you Contestant"
print(sol.truncateSentence(arr,4))