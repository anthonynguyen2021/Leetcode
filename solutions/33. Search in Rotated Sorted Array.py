class Solution:
    # T(n) = O(logn)
    # S(n) = O(1)
    # Explanation: If the target isn't in the middle, check two cases.
    # If the left is sorted, then check if target is in the left half. If not, check the right half.
    # Otherwise, the right half is sorted, then check if the target is in the right half. If not, check the left half.
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        found = -1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[left] <= nums[middle]:
                if nums[left] <= target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle+1
            else:
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return found
​
