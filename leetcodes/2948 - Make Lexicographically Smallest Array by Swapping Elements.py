from typing import List
from collections import deque


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        print(nums)
        
        nums_sorted = sorted(nums)
        
        print(nums_sorted)
        
        nums_to_group = {}
        curr_group = 0  
        nums_to_group[nums_sorted[0]] = curr_group
        
        group_to_nums = {}
        group_to_nums[curr_group] = deque([nums_sorted[0]])
        
        for i in range(1, len(nums_sorted)):
            if abs(nums_sorted[i] - nums_sorted[i-1]) > limit:
                curr_group+=1
                
            nums_to_group[nums_sorted[i]] = curr_group
            
            if curr_group not in group_to_nums:
                group_to_nums[curr_group] = deque()
            group_to_nums[curr_group].append(nums_sorted[i])
            

        ans = []
        for i in range(len(nums)):
            ans.append(group_to_nums[nums_to_group[nums[i]]].popleft())
            
        return ans    
            
        

# Testing locally
if __name__ == "__main__":        
    
    solution = Solution()
    
    nums = [1,7,6,18,2,1]
    limit = 3
    
    print(solution.lexicographicallySmallestArray(nums=nums, limit = limit))