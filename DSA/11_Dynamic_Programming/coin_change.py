"""Coin Change (min coins) – classic DP
Return minimum coins to make amount; -1 if impossible.
"""

def coin_change(coins, amount):
    INF = 10**9
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] < INF else -1


def _test():
    assert coin_change([1,2,5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    print("coin_change OK")


if __name__ == "__main__":
    _test()
