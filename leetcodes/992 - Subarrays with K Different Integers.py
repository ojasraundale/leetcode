from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        print(nums)
        return self.atmostk(nums, k) - self.atmostk(nums, k-1)
        # window_dict = {i:0 for i in range()}
    
    def atmostk(self, nums: List[int], k:int) -> int:
        left = 0
        right = 0
        total = 0
        counts = {}
        
        while right < len(nums):
            counts[nums[right]] = counts.get(nums[right], 0) + 1
            
            while len(counts) > k:
                print(counts)
                counts[nums[left]] -= 1
                if counts[nums[left]] == 0:
                    del counts[nums[left]]
                left += 1
            
            total = total + (right - left + 1)
            right+=1
        return total
    
        
        
    
    
    
# Testing locally

if __name__ == "__main__":
    
    solution = Solution()
    
    nums = [1,2,1,2,3]
    k = 2
    
    print(solution.subarraysWithKDistinct(nums, k))