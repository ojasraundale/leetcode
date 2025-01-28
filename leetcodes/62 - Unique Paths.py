class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # print(m, n)
        grid = [[0 for _ in range(n)] for _ in range(m)]
        # print(grid)
        for i in range(n):
            grid[0][i] = 1
        for i in range(m):
            grid[i][0] = 1    
        # print(grid)
        
        for j in range(1,n):
            for i in range(1,m):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
                
        return grid[m-1][n-1]
        
# Testing locally
if __name__ == "__main__":          
    
    solution = Solution()
    
    m = 3
    n = 7
    
    print(solution.uniquePaths(m, n))