class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumDictionary = {}
        for idx, val in enumerate(nums):
            if target - val in twoSumDictionary:
                twoSumIdx = [twoSumDictionary[target-val], idx]
                break
            twoSumDictionary[val] = idx
        return twoSumIdx
