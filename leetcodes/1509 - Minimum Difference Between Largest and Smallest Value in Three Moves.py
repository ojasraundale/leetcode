from typing import List
import heapq

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        print(nums)
        
        if len(nums) < 5:
            return 0
        
        smallest_four = heapq.nsmallest(4, nums)
        largest_four = sorted(heapq.nlargest(4, nums))
        
        print(smallest_four, largest_four)    
        
        return abs(min(
            largest_four[0] - smallest_four[0],
            largest_four[1] - smallest_four[1],
            largest_four[2] - smallest_four[2],
            largest_four[3] - smallest_four[3],
        ) )
    
        
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    nums = [5,3,2,4]
    
    print(solution.minDifference(nums))