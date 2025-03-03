from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # print(nums)
        
        n_pivot = 0
        
        ans = []
        for num in nums:
            if num < pivot:
                ans.append(num)
            elif num == pivot:
                n_pivot += 1
        
        ans.extend([pivot]*n_pivot)
        
        # print(ans)
        
        for num in nums:
            if num > pivot:
                ans.append(num)
        
        return(ans)
    
    
# Testing locally
if __name__ == "__main__":
    
    nums = [9,12,5,10,14,3,10]
    pivot = 10
    
    solution = Solution()
    
    print(solution.pivotArray(nums, pivot))