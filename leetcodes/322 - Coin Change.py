from typing import List
from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        print(coins)
        
        dp = [float('inf')] * (amount+1)
        
        dp[0] = 1
        
        min_coin = float('inf')
        for coin in coins:
            # dp[coin] = 1
            min_coin = min(min_coin, coin)
        
        
        for i in range(min_coin, amount+1):
            
            current_ans = dp[i]
            for coin in coins:
                if i-coin >= 0:
                    current_ans = min(current_ans, dp[i-coin]+1)
                
            dp[i] = current_ans
            
        return dp[amount]-1 if dp[amount] != float('inf') else -1 
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    
    coins = [1,2,5]
    amount = 11
    
    print(solution.coinChange(coins=coins, amount=amount))