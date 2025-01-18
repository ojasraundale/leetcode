from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        print(derived)
        
        ans = 0
        
        for i in derived:
            ans = ans ^ i
        
        return not(bool(ans))
    
# Testing locally
if __name__ == "__main__":
    
    derived = [1,1,0]
    
    solution = Solution()
    
    print(solution.doesValidArrayExist(derived=derived))