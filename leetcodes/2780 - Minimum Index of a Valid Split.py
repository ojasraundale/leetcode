from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        print(nums)
        counts = {}
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        max_x, max_f = 0, 0
        for x, f in counts.items():
            if f > max_f:
                max_x = x
                max_f = f

        print(max_x, max_f)
        left_doms = 0
        right_doms = max_f
        
        for i in range(0, len(nums)):
            if nums[i] == max_x:
                left_doms += 1
                right_doms -= 1
            
            print(left_doms, right_doms) 
            if (2*left_doms > (i+1)) and (2*right_doms > len(nums) - (i+1)):
                return i
            
        return -1
            
        

# Testing locally

if __name__ == "__main__":
    
    solution = Solution()
    
    nums = [2,1,3,1,1,1,7,1,2,1]
    
    print(solution.minimumIndex(nums))