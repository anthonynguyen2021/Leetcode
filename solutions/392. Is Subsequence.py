class Solution:
    # Time = O(n + m) where n, m are sizes of strings s, t, respectively.
    # Space = O(1)
    # Two Pointer Approach:
    # While the pointers are in bounds, keep moving the second pointer until t[second] == s[first] or when it's out of bounds
    # if second is out of bounds, return False
    # Otherwise, increment both pointers
    # Return first == len(s)
    def isSubsequence(self, s: str, t: str) -> bool:
        first = 0
        second = 0
        while first < len(s) and second < len(t):
            while second < len(t) and t[second] != s[first]:
                second += 1
            if second == len(t):
                return False
            first += 1
            second += 1
        return first == len(s)
