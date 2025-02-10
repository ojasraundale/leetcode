from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # print(amount)
        
        n_rows = len(coins) + 1
        n_cols = amount + 1
        dp = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        
        for i in range(n_rows):
            dp[i][0] = 1
            
        for i in range(n_rows-2, -1, -1):
            for j in range(1, n_cols):
                # print(j)
                if coins[i] > j:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j-coins[i]]
        
        print(dp)
        return dp[0][amount]
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    amount = 5
    coins = [1,2,5]
    
    print(solution.change(amount, coins))