class Solution(object):
    def minPartitions(self, n):
        m=0
        for i in range(9,0,-1):
            if str(i) in n:
                return i