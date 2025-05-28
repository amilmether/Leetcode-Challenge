class Solution(object):
    def leftRightDifference(self, nums):
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        final = [0] * n

        # Compute leftSum
        for i in range(1, n):
            leftSum[i] = leftSum[i - 1] + nums[i - 1]

        # Compute rightSum
        for i in range(n - 2, -1, -1):
            rightSum[i] = rightSum[i + 1] + nums[i + 1]

        # Compute final absolute difference
        for i in range(n):
            final[i] = abs(leftSum[i] - rightSum[i])

        return final

sol = Solution()
arrr = [10, 4, 8, 3]
print(sol.leftRightDifference(arrr))
