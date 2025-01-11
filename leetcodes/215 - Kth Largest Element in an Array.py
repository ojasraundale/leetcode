from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        print(nums, k)
        
        heap = []
        
        for num in nums:
            heapq.heappush(heap, num)
            
            if len(heap) > k:
                heapq.heappop(heap)
             
        return heapq.heappop(heap)                
        # print(heap)
        
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    nums = [3,2,1,5,6,4]
    k = 2
    
    print(solution.findKthLargest(nums=nums, k=k))