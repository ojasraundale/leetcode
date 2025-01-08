from typing import Optional, List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        print(words)
        res = []
        for w1 in words:
            for w2 in words:
                if w1 == w2:
                    continue
                
                if w1 in w2:
                    res.append(w1)    
                    break
        return res
        
        
# Testing locally
if __name__ == "__main__":
    
    
    solution = Solution()
    
    words = ["mass","as","hero","superhero"]
    
    print(solution.stringMatching(words=words))