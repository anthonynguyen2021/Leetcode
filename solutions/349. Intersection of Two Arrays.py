class Solution:
    # Time = O(n + m) - due to the conversion of sets and the helper method filling in the set
    # Space = O(n + m) - due to the set1, set2, and intersection
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        if len(set1) <= len(set2):
            return self.helperIntersection(set1, set2)
        else:
            return self.helperIntersection(set2, set1)
        
    def helperIntersection(self, set1, set2):
        intersection = [x for x in set1 if x in set2]
        return intersection
