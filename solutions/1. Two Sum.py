class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            if (target - nums[i]) in dictionary:
                output =  [dictionary[target-nums[i]], i]
                break
            else:
                dictionary[nums[i]] = i
        return output
