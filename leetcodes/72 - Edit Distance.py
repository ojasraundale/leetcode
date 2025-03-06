from collections import deque
from typing import Optional, List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        print(word1)
        
        l_1 = len(word1)
        l_2 = len(word2)
        
        dp = [[0]*(l_2+1) for _ in range(l_1+1)]
        
        # print(len(dp))
        
        for i in range(l_1+1):
            dp[i][0] = i
        
        for j in range(l_2+1):
            dp[0][j] = j
        
        
        for i in range(1, l_1+1):
            for j in range(1, l_2+1):
            
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j-1],
                        dp[i][j-1],
                        dp[i-1][j],
                    )

        return dp[l_1][l_2]
        # print(dp)
        
        

# Testing locally
if __name__ == "__main__":
    
    word1 = "horse"
    word2 = "ros"
    
    solution = Solution()        
    
    print(solution.minDistance(word1, word2))