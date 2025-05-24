class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        arr1.sort()
        arr2.sort()
        count=0
        j=0
        for i in range(len(arr1)):
            while j < len(arr2) and arr2[j] < arr1[i]-d:
                j+=1
            if j== len(arr2) or arr2[j] > arr1[i]+d:
                count +=1
        return count
sol=Solution()
arr1=[4,5,8]
arr2=[10,9,1,8]
print(sol.findTheDistanceValue(arr1,arr2,2))
        