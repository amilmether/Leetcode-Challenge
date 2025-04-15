class Solution(object):
    def twoSum(self, nums, target):
        flag=0
        pos=[]
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if nums[i]+nums[j]==target:
                    pos.append(i)
                    pos.append(j)
                    flag=1
                    break
            if flag == 1:
                return pos
        
sol=Solution()
arry=[10, 22, 5, 75, 65, 80, 30, 110, 90, 150, 120, 50, 70, 40]
tar=130
print(sol.twoSum(arry,tar))