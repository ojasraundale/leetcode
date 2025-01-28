from typing import List
from collections import deque

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        print(grid)
        
        n_rows = len(grid)
        n_cols = len(grid[0])
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        
        max_sum = 0
        
        def dfs(row, col):
            if 0<=row<n_rows and 0<=col<n_cols:
                if grid[row][col] == 0:
                    return 0
                
                else:
                    dfs_sum = grid[row][col]
                    grid[row][col] = 0
                    for dx, dy in directions:
                        new_row = row+dx
                        new_col = col+dy
                        
                        dfs_sum += dfs(new_row, new_col)
                    return dfs_sum   
            else:
                return 0
    
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] != 0:
                    max_sum = max(max_sum, dfs(row, col))
                
                
        return max_sum
        
        
        
# Testing locally
if __name__ == "__main__":          
    
    solution = Solution()
    
    grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
    
    print(solution.findMaxFish(grid))