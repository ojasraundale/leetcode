from typing import List
from collections import deque

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # print(grid)
        
        q = deque()
        n_rows = len(grid)
        n_cols = len(grid[0])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        cost_mat = [[float('inf') for i in range(n_cols)] for j in range(n_rows)]
        cost_mat[0][0] = 0
        # print(len(cost_mat), len(cost_mat[0]))
        # print(len(grid), len(grid[0]))
        
        q.append([0,0])
        
        def is_valid(row, col):
            if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
                return False
            return True
        
        
        while(q):
            row, col = q.popleft()
            # print(f"row, col: {row, col, cost_mat[row][col]}")
            for dir, (dx, dy) in enumerate(directions):
                new_row = row + dx
                new_col = col + dy
                
                if is_valid(new_row, new_col):
                    # print(f"new row, new col: {new_row, new_col, cost_mat[new_row][new_col]}")
                    
                    cost = 0 if grid[row][col] == dir + 1 else 1
                    
                    if cost_mat[new_row][new_col] > cost_mat[row][col] + cost:
                        cost_mat[new_row][new_col] = cost_mat[row][col] + cost
                        
                        if cost == 1:
                            q.append([new_row, new_col])
                        else:
                            q.appendleft([new_row, new_col])
                        
        return cost_mat[n_rows-1][n_cols-1]
                
            


# Testing locally
if __name__ == "__main__":
    
    grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
    
    solution = Solution()
    
    print(solution.minCost(grid=grid))