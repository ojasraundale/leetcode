from collections import deque
from typing import Optional, List

# 
# 
# abcde
# a
#  

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        
        print(dp)
        
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                print(i,j)
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        print(dp)
        
        return dp[len(text1)][len(text2)]



# Testing locally
if __name__ == "__main__":
    
    text1 = "abcde"
    text2 = "ace" 
    
    solution = Solution()
    
    
    print(solution.longestCommonSubsequence(text1=text1, text2=text2))
    
    


