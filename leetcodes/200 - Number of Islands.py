from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        print(grid)
        
        directions = [[1,0], [0,1], [-1,0], [0, -1]]
        
        n_rows = len(grid)
        n_cols = len(grid[0])
        
        def dfs(i, j):
            if i < 0 or j< 0 or i >=n_rows or j >= n_cols or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            
            for dir_i, dir_j in directions:
                dfs(i+dir_i, j+dir_j)
            
            return
        
        islands = 0
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == "1":
                    islands+=1 
                    dfs(row, col)
                    
        return islands
        
        
        
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    
    print(solution.numIslands(grid=grid))