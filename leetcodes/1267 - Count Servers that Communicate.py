from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        print(grid)
        row_sum = [sum(row) for row in grid]
        col_sum = [sum([row[i] for row in grid]) for i in range(len(grid[0])) ]
        
        total_count = sum(row_sum)
        
        # ans = total_count
        # ans = 0
        # for i in row_sum:
        #     if i>1:
        #         ans+=i
        
        # for i in col_sum:
        #     if i>1:
        #         ans+=i                      
        
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                cell = grid[row][col]
                if cell == 1 and (row_sum[row] > 1 or col_sum[col] > 1):
                    ans += 1
                
        # print(total_count)
        # print(total_count)
        print(row_sum)
        print(col_sum)
        return ans
    
    
# Testing locally
if __name__ == "__main__":
    solution = Solution()    
        
    # grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
    
    grid = [[1,0],[1,1]]
    
    print(solution.countServers(grid))