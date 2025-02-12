from typing import List
import heapq

class Solution:
    
    def sum_of_digits(self, num):
        return sum(map(int, str(num)))
    
    def maximumSum(self, nums: List[int]) -> int:
        print(nums)
        
        digit_dict = {}
        
        print(digit_dict)
        
        for num in nums:
            print(self.sum_of_digits(num))
            sum_digit = self.sum_of_digits(num)
            
            if sum_digit not in digit_dict:
                digit_dict[sum_digit] = [num]
            else:
                heapq.heappush(digit_dict[sum_digit], num)
            
        print(digit_dict)
        
        max_sum = -1
        for i, digit_list in digit_dict.items():
            
            if len(digit_list) >= 2:
                max_sum = max(max_sum, sum(heapq.nlargest(2, digit_list)))
                
        return max_sum
        
            
        
        
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    nums = [18,43,36,13,7]
    nums = [279,169,463,252,94,455,423,315,288,64,494,337,409,283,283,477,248,8,89,166,188,186,128]
    
    print(solution.maximumSum(nums))
    
    
