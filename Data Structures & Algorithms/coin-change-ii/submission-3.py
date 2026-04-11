class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        prev = [0]*(amount+1)
        coins.sort()

        prev[0] = 1
        
        for i in range(len(coins)):
            cur = [0]*(amount+1)
            cur[0] = 1
            for a in range(1, amount+1):
                cur[a] = prev[a]
                if a >= coins[i]:
                    cur[a] += cur[a-coins[i]]
            prev = cur
        
        return prev[amount]