class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time = O(n log n) to sort
        # Space = O(n) to store these intervals
        # Sort the components in intervals via first component using a lambda function
        intervals.sort(key = lambda x : x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
        
