from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # print(target)
        
        row_i = 0
        row_j = len(matrix)
        
        if target < matrix[0][0] or target>matrix[-1][-1]: 
            return False
        
        while row_i<= row_j:
            mid = (row_j+row_i)//2
            print(row_i, row_j, mid)
            
            if target > matrix[mid][-1]:
                row_i = mid+1
            elif target < matrix[mid][0]:
                row_j = mid-1
            else: 
                break
            
        if row_i > row_j:
            return False
        
        row = (row_j + row_i)//2
        
        col_i = 0
        col_j = len(matrix[0])
        
        while col_i<=col_j:
            mid = (col_j+col_i)//2
            if matrix[row][mid] > target:
                col_j = mid - 1
            elif matrix[row][mid] < target: 
                col_i = mid + 1
            else: 
                return True
        return False
        
        # print(row_i)
            
    
    

    
# Testing locally
if __name__ == "__main__":
    
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
    target = 11
    
    solution = Solution()
    
    print(solution.searchMatrix(matrix=matrix, target=target))
    