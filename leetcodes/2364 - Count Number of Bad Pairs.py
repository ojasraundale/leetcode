from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # print(nums)
        
        # bad_pairs = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
                
        #         if j-i != nums[j] - nums[i]:
        #             bad_pairs+=1
        
        # return bad_pairs                
        
        diff_with_self_map = {}
        
        for i in range(len(nums)):
            diff_with_self_map[nums[i] - i] = 1 + diff_with_self_map.get(nums[i] - i, 0)
            
        good_pairs = 0
        
        for diff, vals in diff_with_self_map.items():
            print(f"diff, vals, good_pair = {diff, vals, (vals * (vals - 1))/2}")
            good_pairs += (vals * (vals - 1))/2
        
        
        print(good_pairs)
        bad_pairs = (len(nums)*(len(nums)-1))/2 - good_pairs
        return bad_pairs            
            
        # print(diff_with_self_map)
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    nums = [4,1,3,3]
    
    print(solution.countBadPairs(nums))
    
    