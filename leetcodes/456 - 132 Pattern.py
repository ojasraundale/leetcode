from typing import Optional, List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        print(nums)
        
        # res = False
        
        # lowest = float('infinity')
        # highest = -float('inf')
        
        # lowest_temp = float('infinity')
        # highest_temp = -float('inf')
        
        # print(lowest, highest)
        
        # in_inc_subsequence = False
        # for i in range(len(nums) - 2):
        #     if nums[i] < nums[i+1]:
        #         in_inc_subsequence = True
        #         lowest_temp = min(lowest, nums[i])
        #         highest_temp = max(highest, nums[i+1])
                
                
        #         if lowest_temp < lowest and highest_temp > highest:
        #             lowest = lowest_temp
        #             highest = highest_temp
                    
        #         if in_inc_subsequence:
        #             highest = max(highest, highest_temp)

        #     else:
        #         in_inc_subsequence = False
            
        #     print(f"i: {i}, lowest: {lowest}, highest: {highest}")                
            
            
        #     if nums[i+2] > lowest and nums[i+2] < highest:
        #         return True
        
        
        stack = []
        curmin = nums[0]
        
        stack.append((nums[0], curmin))
        
        for i in range(1, len(nums)):
            while stack and stack[-1][0] <= nums[i]:
                stack.pop()
            
            if stack and stack[-1][1] < nums[i]:
                return True
            
            stack.append((nums[i], curmin))
            
            
            curmin = min(curmin, nums[i])
            
            
            
        return False
            
            
        
        
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    nums = [1,4,0,-1,-2,-3,-1,-2]
    
    # nums = [3,1,4,2]
        
    # nums = [-2,1,2,-2,1,2]
    
    print(solution.find132pattern(nums=nums))