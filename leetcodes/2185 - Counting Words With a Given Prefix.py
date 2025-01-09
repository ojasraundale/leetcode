from typing import Optional, List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        print(words)
        
        res = 0
        
        for word in words:
            if word.startswith(pref):
                res+=1

        return res
        
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    words = ["pay","attention","practice","attend"]
    pref = "at"
    
    print(solution.prefixCount(words, pref))