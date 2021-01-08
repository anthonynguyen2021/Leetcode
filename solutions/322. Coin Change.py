class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time = size(coins) * size(range(amount+1))
        # Space = size(range(amount+1))
        numCoins = [float('inf') for i in range(0, amount+1)]
        numCoins[0] = 0
        for denom in coins:
            for money in range(1, amount+1):
                if denom <= money:
                    numCoins[money] = min(numCoins[money], 1 + numCoins[money-denom])
        return numCoins[-1] if numCoins[-1] != float('inf') else -1
