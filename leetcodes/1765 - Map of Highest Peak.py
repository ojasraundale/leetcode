from typing import List
from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        print(isWater)
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        n_rows = len(isWater)
        n_cols = len(isWater[0])
        
        
        res = [[-1 for _ in range(n_cols)] for _ in range(n_rows)]
        
        # print(res)
        
        q = deque()
        
        for row in range(n_rows):
            for col in range(n_cols):
                if isWater[row][col] == 1:
                    res[row][col] = 0
                    q.append((row, col, 0))
                    
        while q:
            row, col, h = q.popleft()
            
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                
                if 0 <= new_row < n_rows and 0 <= new_col < n_cols:
                    if res[new_row][new_col] == -1:
                        res[new_row][new_col] = h + 1
                        q.append((new_row, new_col, h + 1))
            
        return res
        
        
    
# Testing locally
if __name__ == "__main__":
    solution = Solution()
    isWater = [[0,1],[0,0]]
    # isWater = [[0,1],[0,0], [1,1]]
    
    print(solution.highestPeak(isWater=isWater))
        