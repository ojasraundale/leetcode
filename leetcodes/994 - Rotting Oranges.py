from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        print(grid)
        
        directions = [[-1, 0], [0,- 1], [1, 0], [0, 1]]
        
        n_rows = len(grid)
        n_cols = len(grid[0])

        rotten_q = deque()        
        minute = 0
        
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 2:
                    rotten_q.append((row, col, minute))
          
        print(rotten_q)          
        while rotten_q:
            row, col, minute = rotten_q.popleft()
            
            for dx, dy in directions:
                neighbour_row = row + dx
                neighbour_col = col + dy
                
                if 0<=neighbour_row<n_rows and 0<=neighbour_col<n_cols:
                    if grid[neighbour_row][neighbour_col] == 0:
                        pass
                    elif grid[neighbour_row][neighbour_col] == 1:
                        grid[neighbour_row][neighbour_col] = 2
                        rotten_q.append((neighbour_row, neighbour_col, minute+1))
                    else:
                        pass
        
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 1:
                    return -1
                        
        return minute
                        
        
            
        
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    
    print(solution.orangesRotting(grid=grid))