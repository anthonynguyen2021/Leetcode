class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation = []
        return self.helperPermute(nums, permutation, 0)
    
    def helperPermute(self, nums, permutation, index):
        if index == len(nums) - 1:
            permutation.append(nums[:])
        for idx in range(index, len(nums)):
            self.swap(nums, index, idx)
            self.helperPermute(nums, permutation, index + 1)
            self.swap(nums, index, idx)
        return permutation
        
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        return 
