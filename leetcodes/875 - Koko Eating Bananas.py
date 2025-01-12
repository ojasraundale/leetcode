from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # print(piles)
        
        max_ = max(piles)
        min_ = min(piles)
        i = 1
        # i = min_
        j = max_
        
        ans = max_

        while i<=j:
            mid = int((i+j)/2)
            sum_i = sum([int(x/mid) if x%mid == 0 else int(x/mid) + 1 for x in piles])
            
            if sum_i > h:
                i = mid+1
            else:
                j = mid - 1
                ans = mid
        
        return ans

    
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    piles = [3,6,7,11]
    h = 8



    print(solution.minEatingSpeed(piles=piles, h=h))