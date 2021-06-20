# DP Approach: Time = O(mn) | Space = O(n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        numSolutionDP = [1 for i in range(n)]
        for idx in range(1, m):
            for idx2 in range(1, n):
                numSolutionDP[idx2] += numSolutionDP[idx2-1]
        return numSolutionDP[-1]
