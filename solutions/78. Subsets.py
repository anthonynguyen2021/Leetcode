class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time = O(n 2^n)
        # Space = O(n 2^n)
        powerSet = [[]]
        for val in nums:
            powerSet += [[val] + elemSet for elemSet in powerSet]
        return powerSet 
