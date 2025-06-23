class Solution(object):
    def plusOne(self, digits):
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i]=0
        return [1] + digits
sol=Solution()
arr=[1,2,3]
print(sol.plusOne(arr))