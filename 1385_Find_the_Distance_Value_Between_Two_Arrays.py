class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count=0
        for num1 in arr1:
            is_far=True
            for num2 in arr2:
                if abs(num1-num2) <=d:
                    is_far=False
                    break
            if is_far:
                count+=1
        return count

sol=Solution()
arr1=[4,5,8]
arr2=[10,9,1,8]
print(sol.findTheDistanceValue(arr1,arr2,2))
        