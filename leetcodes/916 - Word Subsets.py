from typing import Optional, List

class Solution:
    
    # def isSubset(self, word1, word2):
    #     pass
     
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        print(words1, words2)
        res = []
        
        words2_dict = {chr(ord('a')+i):0 for i in range(26) }
        
        # print(words2_dict)
        for w in words2:
            w_count = {chr(ord('a')+i):0 for i in range(26) }
            for s in w:
                w_count[s]+= 1
            
            for letter in [chr(ord('a')+i) for i in range(26)]:
                words2_dict[letter] = max(words2_dict[letter], w_count[letter])
                
            
        # print(words2_dict)
        
        for w in words1:
            w_count = {chr(ord('a')+i):0 for i in range(26) }
            for s in w:
                w_count[s]+= 1
            
            to_consider = True
            for letter in [chr(ord('a')+i) for i in range(26)]:
                if w_count[letter] < words2_dict[letter]:
                    to_consider = False
                    break
            if to_consider:
                res.append(w)
            
        return res
        # print
                
            
            
                
        
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    words1 = ["amazon","apple","facebook","google","leetcode"]
    # words2 = ["e","oo", "o"]    
    words2 = ["e","o"]    
    
    print(solution.wordSubsets(words1=words1, words2=words2))