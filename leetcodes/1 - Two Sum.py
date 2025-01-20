from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i, num in enumerate(nums):
            if target-num in hashmap:
                return hashmap[target-num], i
            hashmap[num] = i
            
            
        
        
# Testing locally
if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    
    solution = Solution()
    
    print(solution.twoSum(nums=nums, target=target))