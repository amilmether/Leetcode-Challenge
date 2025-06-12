from collections import defaultdict
class Solution(object):
    def mostFrequent(self,nums, key):
        count = defaultdict(int)
        for i in range(len(nums)-1):
            if nums[i] == key:
                count[nums[i+1]] += 1
        return max(count,key=count.get)