class Solution:
    # Time = {n choose k} x k + {n choose k-1} + ... + {n choose 0} 
    # Go through all l-subsets where l in {1, ..., k} and append {n choose k} k-subsets
    # Space = {n choose k} x k
    def combine(self, n: int, k: int) -> List[List[int]]:
        combination = []
        self.helperCombination(n, k, 1, combination, [])
        return combination
    
    def helperCombination(self, n, k, i, combination, current):
        if len(current) == k:
            combination.append(current)
        else:
            if i == n+1:
                return
        for j in range(i, n+1):
            self.helperCombination(n, k, j+1, combination, current + [j])
        return 
