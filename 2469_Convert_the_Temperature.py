class Solution(object):
    def convertTemperature(self, celsius):
        kelvin =celsius + 273.15
        fahrenheit= (celsius * 1.80 )+32.00
        ans=[round(kelvin, 5),round(fahrenheit,5)]
        return ans

sol=Solution()
print(sol.convertTemperature(36.50))