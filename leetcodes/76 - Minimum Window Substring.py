from typing import Optional, List

class Solution:
    def checkvalidity(self, hash_window, hash_t):
        for key,val in hash_t.items():
            if hash_window.get(key, 0) < hash_t.get(key, 0):
                return False
            
        return True
    
    def minWindow(self, s: str, t: str) -> str:
        print(s,t)
        
        hash_t = {}
        for char_t in t:
            hash_t[char_t] = 1 + hash_t.get(char_t, 0)
        
        hash_s = {}
        for char_s in s:
            hash_s[char_s] = 1 + hash_s.get(char_t, 0)
        print(hash_t)
        print(hash_s)
        print(self.checkvalidity(hash_window=hash_s, hash_t=hash_t))
        
        
        hash_window = {}
        
        l = 0
        res_l, res_r, res_len = -1,-1,float("infinity")
        
        for r in range(len(s)):
            hash_window[s[r]] = 1 + hash_window.get(s[r], 0)
            while self.checkvalidity(hash_window=hash_window, hash_t=hash_t):
                
                print(f"hash_window: {hash_window}")
                if r-l+1 < res_len:
                    res_l = l
                    res_r = r
                    res_len = r-l+1 
                
                hash_window[s[l]] -= 1
                l+= 1
        
        return s[res_l:res_r+1] if res_len!= float("infinity") else ""
                
                
        
        
        

        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    s = "ADOBECODEBANC"
    t = "ABC"
    
    print(solution.minWindow(s=s,t=t))