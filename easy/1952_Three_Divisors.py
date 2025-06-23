
import math
class Solution(object):
    def isThree(self,n):
        divisor_count =0
        if n<=0:
            return False
        sqrt_n = int(math.sqrt(n))
        if sqrt_n * sqrt_n != n:
            
            return False
            
        for i in range(2, int(math.sqrt(sqrt_n))+ 1):
            if sqrt_n % i ==0:
                return False