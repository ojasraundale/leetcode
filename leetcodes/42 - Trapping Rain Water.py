from typing import List
from collections import deque

class Solution:
    def trap(self, height: List[int]) -> int:
        print(height)
        
        left_max = 0
        right_max = 0
        
        left_arr = [0] * len(height)
        right_arr = [0] * len(height)
        
        Volume = 0
        
        for i in range(len(height)):
            left_arr[i] = left_max
            left_max = max(left_max, height[i])
        
        for i in range(len(height)-1, -1, -1):
            right_arr[i] = right_max
            right_max = max(right_max, height[i])
            
            
        print(left_arr)
        print(right_arr)
        
        for i in range(len(height)):
            dV = min(left_arr[i], right_arr[i]) - height[i]
            if dV>0:
                print(f"dV = {dV}")
                Volume += dV
            
        return Volume
        
            
            
        
# Testing locally
if __name__ == "__main__":
    
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height = [0,2,0,3,1,0,1,3,2,1]
    
    solution = Solution()
    
    print(solution.trap(height))