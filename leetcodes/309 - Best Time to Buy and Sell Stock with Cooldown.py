from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        states = {}
        
        
        
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in states:
                return states[(i, buying)]
            
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                cd = dfs(i+1, buying)
                states[(i, buying)] = max(buy, cd)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                cd = dfs(i+1, buying)
                states[(i, buying)] = max(sell, cd)
                
            return states[(i, buying)]
                
        return dfs(0, True)
    
    
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    prices = [1,2,3,0,2]
    
    print(solution.maxProfit(prices))