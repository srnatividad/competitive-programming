class Solution:
    def change(self, amount, coins) -> int:
        memo = [0] * (amount+1)
        memo[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                memo[i] += memo[i-coin]

        return memo[amount]