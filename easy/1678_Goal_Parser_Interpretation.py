import re
class Solution(object):
    def interpret(self, command):
        command = command.replace("()" , "o")
        command = command.replace("(al)","al")
        return command

                

sol=Solution()
print(sol.interpret("G()(al)"))