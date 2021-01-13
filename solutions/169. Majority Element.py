class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Time = O(n)
        # Space = O(1)
        # Idea of the solution: Initiate the first element as the candidate to the majority problem
        # If the next is not the same as the candidate, decrease our count. Otherwise increase it. 
        # Whenever the count = 0, set the current number as the candidate.
        # Mathematical proof: If any two adjacent elements are distinct, we can remove them and the 
        # majority element is still the same. By backward induction, we have an array of just the majority element.
        candidateCount = 0
        for idx in range(len(nums)):
            if candidateCount == 0:
                candidate, candidateCount = nums[idx], candidateCount + 1
            elif candidate != nums[idx]:
                candidateCount -= 1
            else:
                candidateCount += 1
        return candidate
