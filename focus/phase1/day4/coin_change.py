def minimum_coin(target, coins, memo={}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None

    for coin in coins:
        remainder = target - coin
        remainderResult = minimum_coin(remainder, coins, memo)
        if remainderResult != None:
            memo[target] = remainderResult + [coin]
            return memo[target]
        
    memo[target] = None
    return None


if __name__ == "__main__":
    test_cases = int(input())
    for tc in range(1, test_cases + 1):
        coins = [20,10,5,1]
        target = int(input())

        res = minimum_coin(target, coins)
        print(len(res))