class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Time = O(n)
        # Space = O(1)
        candidateCount = 0
        for idx in range(len(nums)):
            if candidateCount == 0:
                candidate, candidateCount = nums[idx], candidateCount + 1
            elif candidate != nums[idx]:
                candidateCount -= 1
            else:
                candidateCount += 1
        return candidate
