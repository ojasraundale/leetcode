from typing import Optional, List

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        print(k)
        
        if k > len(s):
            return False
        if k == len(s):
            return True

        s_dict = {chr(ord('a')+i): 0 for i in range(26)}
        
        for c in s:
            s_dict[c]+=1
            
        odd_freqs = 0
        for c,freq in s_dict.items():
            if freq%2 == 1:
                odd_freqs+=1
        
        if k < odd_freqs:
            return False
        
        return True
        
        
    
    
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    s = "leetcode"
    k = 3
    print(solution.canConstruct(s=s, k=k))


