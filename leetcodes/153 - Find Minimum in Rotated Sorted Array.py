from typing import List
from collections import deque

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # 4, 5, 6, 1 ,2, 3
        
        # 6, 1, 2, 3, 4, 5
        
        
        print(nums)
        l = 0
        r = len(nums) - 1
        
        while l<=r:
            mid = (l+r)//2
            
            print(f"l, mid, r = {l, mid, r}")
            
            if  (mid+1 < len(nums)) and (nums[mid] > nums[mid+1]):
                print(f"Returning mid + 1")
                return nums[mid+1]
            
            if  (mid-1 >= 0) and  nums[mid] < nums[mid-1]:
                print(f"Returning mid - 1")
                return nums[mid]
            
            if nums[l] < nums[mid] and nums[mid] > nums[r]:
                l = mid+1
            
            else:
                r = mid - 1
        
        return nums[l]
        
        
        
# Testing locally
if __name__ == "__main__":          
    
    nums = [3,4,5,1,2]
    
    nums =[4,5,6,7]
    
    nums=[4,5,0,1,2,3]
    
    nums=[1]
    
    solution = Solution()
    
    print(solution.findMin(nums))