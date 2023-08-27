class Solution:
    def __init__(self):
        self.memo = {}

    def coinChange(self, coins, amount) -> int:
        if amount == 0: return 0

        ans = self.dp(coins, amount)
        if ans == None or sum(ans) != amount: return -1
        else: return len(ans)

    # Top-down
    def dp(self, coins, amount):
        if amount in self.memo: return self.memo[amount]
        if amount == 0: return []
        if amount < 0: return None

        shortestCombi = None

        for coin in coins:
            remaining = amount - coin
            remainingResult = self.dp(coins, remaining)
            if remainingResult != None:
                combination = remainingResult + [coin]
                if shortestCombi == None or len(combination) < len(shortestCombi):
                    shortestCombi = combination

        self.memo[amount] = shortestCombi
        return shortestCombi