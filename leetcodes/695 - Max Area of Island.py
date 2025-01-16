from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [0,1], [-1,0], [0, -1]]
        
        n_rows = len(grid)
        n_cols = len(grid[0])
        
        print(n_rows, n_cols)
        def dfs(i, j):
            if i < 0 or j< 0 or i >=n_rows or j >= n_cols or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            dfs_area = 1
            
            for dir_i, dir_j in directions:
                dfs_area += dfs(i+dir_i, j+dir_j)
            
                # print(dfs_area)
            return dfs_area
        
        max_area = 0
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 1:
                    # islands+=1 
                    area = dfs(row, col)
                    # print(area)
                    max_area = max(max_area, area)
                    
        return max_area
    

# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    
    print(solution.maxAreaOfIsland(grid=grid))