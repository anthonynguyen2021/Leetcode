class Solution:
    # Solution is based on Memoization - Cache the solution at the previous solution to avoid reptitively function calls
    def fib(self, n: int) -> int:
        return self.helperFib(n)
    
    def helperFib(self, n, memoize = {0 : 0, 1 : 1}):
        if n in memoize:
            return memoize[n]
        memoize[n] = self.helperFib(n-2, memoize) + self.helperFib(n-1, memoize)
        return memoize[n]
