from typing import Optional, List

class Solution:
    def countSubstrings(self, s: str) -> int:
        # print(s)
        
        res = 0
        
        ## Odd strings
        for i in range(len(s)):
            j = 0
            while i-j>=0 and i+j<len(s):
                if s[i-j] == s[i+j]:
                    res+= 1
                    j+=1
                else:
                    break
        
        ## Even strings
        
        for i in range(len(s)-1):
            j = 0
            while i-j>=0 and i+j+1<len(s):
                if s[i-j] == s[i+1+j]:
                    res+= 1
                    j+=1
                else:
                    break
                
        return res
                
            
        
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    s = "aaa"
    
    print(solution.countSubstrings(s))
        