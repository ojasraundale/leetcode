from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        print(numbers)
        
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            if numbers[l] + numbers [r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers [r] < target:
                l+=1
            elif numbers[l] + numbers [r] > target:
                r-=1
        
        return -1
        
# Testing locally
if __name__ == "__main__":
    solution = Solution()   
    
    numbers = [2,7,11,15]
    target = 9
    
    print(solution.twoSum(numbers=numbers, target=target))