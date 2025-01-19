from typing import List
import heapq

class Solution:
    
    class Cell:
        def __init__(self, height, row, col):
            self.height = height
            self.row = row
            self.col = col
        
        def __lt__(self, other):
            return self.height < other.height
        
        def __str__(self):
            return f"{(self.height, self.row, self.col)}"
            # return (self.height, self.row, self.col)
        
        def __repr__(self):
            return f"{(self.height, self.row, self.col)}"

        
        
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n_rows = len(heightMap)
        n_cols = len(heightMap[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        
        def is_valid(self, row, col):
            return 0<=row<n_rows and 0<=col<n_cols
        
        boundary = []
        
        visited = [[False] * n_cols for i in range(n_rows)]
        
        # First and Last Row in boundary
        
        for col in range(n_cols):
            heapq.heappush(boundary, self.Cell(heightMap[0][col], 0, col))
            heapq.heappush(boundary, self.Cell(heightMap[n_rows-1][col], n_rows-1, col))
            visited[0][col] = True
            visited[n_rows-1][col] = True
            
        for row in range(n_rows):
            heapq.heappush(boundary, self.Cell(heightMap[row][0], row, 0))
            heapq.heappush(boundary, self.Cell(heightMap[row][n_cols-1], row, n_cols-1))
            visited[row][0] = True
            visited[row][n_cols-1] = True
            # heapq.heappush(boundary, self.Cell(heightMap[n_rows-1][col], n_rows-1, col))
            
        # print(boundary)
        
        Volume = 0
        while(boundary):
            cell = heapq.heappop(boundary)
            row = cell.row
            col = cell.col
            current_height = cell.height
            
            for dx, dy in directions:
                new_row = row + dx 
                new_col = col + dy
                
                if (is_valid(self, new_row, new_col) and not visited[new_row][new_col]):
                    new_height = heightMap[new_row][new_col]
                    dV = current_height-new_height
                    if dV > 0:
                        Volume+= dV
                        
                    visited[new_row][new_col] = True
                    heapq.heappush(
                        boundary, 
                        self.Cell(
                            max(current_height, new_height), 
                            new_row, 
                            new_col
                            )
                        )
        return Volume
# Testing locally
if __name__ == "__main__":
    
    heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    
    
    solution = Solution()
    
    print(solution.trapRainWater(heightMap=heightMap))