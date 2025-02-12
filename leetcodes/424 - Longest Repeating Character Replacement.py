from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        print(s)
        
        window_dict = {chr(ord('A')+i):0 for i in range(26)}
        
        def highest_freq(window_dict):
            return max(window_dict.items(), key=lambda x: x[1])[1]
        
        print(highest_freq(window_dict))
        l = 0
        # r = 0
        
        ans = 0
        for r in range(len(s)):  # Iterate `r` directly from 0 to len(s)-1
            window_dict[s[r]] += 1  # Expand the window
            
            # Compute the most frequent character count
            high_freq = highest_freq(window_dict)
            
            # If the remaining characters to be replaced exceed k, shrink window
            while (r - l + 1) - high_freq > k:
                window_dict[s[l]] -= 1
                l += 1  # Shrink from the left
            
            # Update max length
            ans = max(ans, r - l + 1)
            
        return ans
        print(window_dict)
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    s = "AABABBA"
    s = "AAAA"
    k = 0
    
    print(solution.characterReplacement(s, k))