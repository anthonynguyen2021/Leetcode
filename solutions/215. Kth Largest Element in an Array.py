import heapq
​
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time = O(n log k) - 
        # Space = O(k)
        # Exaplanation of solution:
        # 1. We work with a min heap is size k. For each element of nums from 1, ..., n, we insert it in O(log k). If the element we're about to insert is larger than the min of the minheap, pop it and insert it. So we do this process n times. So
        # O(n log k)
        # Space is k since we're just tracking the k largest as we go along.
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]  # heapq.nlargest(k, nums) just returns a max [ak, ak-1, .... , a1] where ak is largest.
