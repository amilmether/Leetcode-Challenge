class Solution(object):
    def majorityElement(self, nums):
        elem = None
        count = 0
        for num in nums:
            if count == 0:
                elem = num
                count = 1
            elif num == elem:
                count += 1
            else:
                count -= 1
        return elem
