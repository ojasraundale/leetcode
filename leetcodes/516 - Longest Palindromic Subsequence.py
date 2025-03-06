from typing import Optional, List


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # print(s)
        
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
            
        
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                # print(i,j)
                # print(s[i], i, s[j], j)
                if s[i] == s[j]:
                    # print("wow")
                    dp[i][j] = dp[i+1][j-1] + 2
                else: 
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # print(dp)
        return dp[0][n - 1]
                    


# Testing locally
if __name__ == "__main__":
    
    s = "bbbab"
    
    solution = Solution()        
    print(solution.longestPalindromeSubseq(s))
    