from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # print(arr)
        
        map = {}
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                map[mat[row][col]] = [row, col]
                
        # print(map)

        row_remaining = [len(mat[0]) for i in range(len(mat))]
        col_remaining = [len(mat) for i in range(len(mat[0]))]
        
        # print(row_remaining)
        for i, num in enumerate(arr):
            row, col = map[num]
            
            row_remaining[row] += -1
            col_remaining[col] += -1
            
            if row_remaining[row] == 0 or col_remaining[col] == 0:
                return i
        return -1
    
# Testing locally
if __name__ == "__main__":
    arr = [2,8,7,4,1,3,5,6,9]
    mat = [[3,2,5],[1,4,6],[8,7,9]]
    
    solution = Solution()
    
    print(solution.firstCompleteIndex(arr=arr, mat=mat))