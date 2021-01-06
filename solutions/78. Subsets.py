class Solution:
    # T(n) = O(n 2^n)
    # S(n) = O(n 2^n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for val in nums:
            subsets += [[val] + item for item in subsets]  # The order of list concatentation item + [val] is important 
        return subsets
