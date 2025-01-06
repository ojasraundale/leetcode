from typing import Optional, List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(s)
        l=0
        r=0
        unique_charac = set()
        res = 0
        
        
        while r<len(s):
            while s[r] in unique_charac:
                unique_charac.remove(s[l])
                l+=1
            unique_charac.add(s[r])
            res = max(res, r-l+1)
            
            
            r+=1
        
        

        return res
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    s = "pwwkew"
    
    print(solution.lengthOfLongestSubstring(s=s))