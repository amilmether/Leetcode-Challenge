class Solution(object):
    def averageValue(self, nums):
        count=0
        result=0
        for n in nums:
            if n%2==0 and n%3==0:
                result+=n
                count+=1
        if count==0:
            return 0
        else:
            return int(result/count)
            
solution=Solution()   
nums = [2, 6, 9, 18, 24, 30]
print(solution.averageValue(nums))