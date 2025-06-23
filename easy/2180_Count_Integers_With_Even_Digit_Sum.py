class Solution(object):
    def countEven(self, num):
        digit_sum=sum(int(d) for d in str(num))
        return num // 2 if digit_sum % 2 == 0 else (num-1) // 2
sol=Solution()
print(sol.countEven(30))