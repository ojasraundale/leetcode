# https://neetcode.io/problems/islands-and-treasure
from typing import List
from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()
        
        n_rows = len(grid)
        n_cols = len(grid[0])
        
        
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 0:
                    q.append((row, col, grid[row][col]))
        
        
        # def add_bfs_queue(row, col, level):
            
                            
        while q:
            row, col, level = q.popleft()

            
            for dir_r, dir_c in directions:
                new_row = row + dir_r
                new_col = col + dir_c
                
                if ( new_row >= n_rows or new_row<0 or 
                    new_col>= n_cols or new_col<0 or 
                    grid[new_row][new_col] == -1 or 
                    grid[new_row][new_col] < level+1):
                    pass
                else:
                    grid[new_row][new_col] = level + 1
                    q.append((new_row, new_col, level + 1))
                    
        return grid
                    
                
        print(q)
            
        print(grid)
        
        
# Testing locally
if __name__ == "__main__":
    
    derived = [1,1,0]
    
#     grid = [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]

    grid = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    solution = Solution()
    
    print(solution.islandsAndTreasure(grid=grid))