class Solution(object):
    def convertTemperature(self, celsius):
        ans=[celsius + 273.15,(celsius * 1.80 )+32.00]
        return ans

sol=Solution()
print(sol.convertTemperature(36.50))