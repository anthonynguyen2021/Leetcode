class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for idx in range(len(nums)):
            if idx == 0 or nums[idx-1] != nums[idx]:
                self.twoSum(idx, nums, triplets)
        return triplets
    
    def twoSum(self, idx, nums, triplets):
        left, right = idx + 1, len(nums) - 1
        while left < right:
            sum3 = nums[idx] + nums[left] + nums[right]
            if sum3 < 0:
                left += 1
            elif sum3 > 0:
                right -= 1
            else:
                triplets.append([nums[idx], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left-1] == nums[left]:
                    left += 1
        return 
        
