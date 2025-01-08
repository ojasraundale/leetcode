from typing import Optional, List

class Solution:
    
    def isPrefixSuffix(self, word1: str, word2: str):
        ### Checks if word1 is prefix and suffix of word2
        
        if len(word1) > len(word2):
            return False
        
        if word2.startswith(word1) and word2.endswith(word1):
            return True
        
        return False
        
    
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        print(words)
        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                
                if self.isPrefixSuffix(word1=words[i], word2=words[j]):
                    count+=1
                    
        return count
                
        

# Testing locally
if __name__ == "__main__":
    
    
    solution = Solution()
    
    words = ["a","aba","ababa","aa"]
    
    print(solution.countPrefixSuffixPairs(words=words))