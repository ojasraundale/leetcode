class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        print(s)
        
        word_dict = {}
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j+1]
                word_dict[sub] = word_dict.get(sub, 0) + 1
                # print(sub)
        
        longest_sub = None
        longest_len = 0
        for sub, count in word_dict.items():
            if count>1 and len(sub) > longest_len:
                longest_sub = sub
                longest_len = len(sub)
                
        print(longest_sub)
        return longest_len
        
# Testing locally
if __name__ == "__main__":
    
    s = "aabcaabdaab"
    
    solution = Solution()        
    
    print(solution.longestRepeatingSubstring(s))