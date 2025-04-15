from typing import List, Optional

class Solution:
    def maxArea(self, height: List[int]) -> int:
        print(height)
        
        l = 0
        r = len(height) - 1
        
        ans = -1
        while r-l>=0:
            print(f"r,l : {r,l}")
            vol = (r-l) * min(height[r],height[l])
            ans = max(ans, vol)
            
            if height[r]<height[l]:
                r-=1
            else:
                l+=1
                
        return ans
        
        
if __name__ == "__main__":
    solution = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    
    print(solution.maxArea(height))