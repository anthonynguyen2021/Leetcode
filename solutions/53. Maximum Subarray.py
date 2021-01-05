class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        current = 0
        for i in range(len(nums)):
            current += nums[i]
            if current > maxSum:
                maxSum = current
            if current < 0:
                current = 0
        return maxSum 
