from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        print(grid)
        n = len(grid)
        print(n)
        num_list = [0]*(n*n)
        # print(num_list)
        
        for i in range(n):
            for j in range(n):
                print(grid[i][j])
                num_list[grid[i][j]-1] += 1
        
        a=None
        b=None
        for num, count in enumerate(num_list):
            if count == 2:
                a = num+1
            elif count == 0:
                b = num+1
        
        return a,b
        

# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    grid = [[9,1,7],[8,9,2],[3,4,6]]
    
    print(solution.findMissingAndRepeatedValues(grid))