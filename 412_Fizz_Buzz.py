class Solution(object):
    def fizzBuzz(self,n):
        res = []
        for i in range(1, n + 1):
            output = ""
            if i % 3 == 0:
                output += "Fizz"
            if i % 5 == 0:
                output += "Buzz"
            res.append(output if output else str(i))
        return res

solution=Solution()   
print(solution.fizzBuzz(1))