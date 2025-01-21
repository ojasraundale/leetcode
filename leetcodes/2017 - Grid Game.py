from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        print(grid)
        
        top_prefix = [0 for i in range(len(grid[0]))] 
        bot_prefix = [0 for i in range(len(grid[0]))]
        
        top_postfix = [0 for i in range(len(grid[0]))] 
        bot_postfix = [0 for i in range(len(grid[0]))]
        
        sum_top = 0
        sum_bot = 0
        for i in range(len(grid[0])):
            sum_top += grid[0][i]
            top_prefix[i] = sum_top
            
            sum_bot += grid[1][i]
            bot_prefix[i] = sum_bot
            
        sum_top = 0
        sum_bot = 0
        for i in range(len(grid[0])-1, -1, -1):
            sum_top += grid[0][i]
            top_postfix[i] = sum_top
            
            sum_bot += grid[1][i]
            bot_postfix[i] = sum_bot
        
        
        robo_1 = []
        for i,j in zip(top_prefix, bot_postfix):
            robo_1.append(i+j)
        
        print(robo_1)
        
        robo_2 = []
        
        for i, robo_1_score in enumerate(robo_1):
            robo_2.append( max(bot_prefix[i] - grid[1][i], top_postfix[i] - grid[0][i]) )
        
        return min(robo_2)            
        
            
    
# Testing locally
if __name__ == "__main__":
    solution = Solution()
    grid = [[3,3,1],[8,5,2]]
    print(solution.gridGame(grid=grid))