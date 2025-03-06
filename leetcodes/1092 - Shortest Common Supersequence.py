class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        print(str1)
        
        cols = len(str1) + 1
        rows = len(str2) + 1
        dp = [[""]*cols for _ in range(rows)]
        
        for row in range(rows):
            dp[row][cols-1] = str2[row:]
            
        for col in range(cols):
            dp[rows - 1][col] = str1[col:]
        
        for row in range(rows-2, -1, -1):
            for col in range(cols-2, -1, -1):
                # print(row, col)
                if str1[col] == str2[row]:
                    dp[row][col] = str1[col] + dp[row+1][col+1]
                
                else:
                    option_1 = dp[row][col+1]
                    option_2 = dp[row+1][col]
                    if len(option_1) < len(option_2):
                        dp[row][col] = str1[col] + option_1
                    else:
                        dp[row][col] = str2[row] + option_2
        
        # print(dp)
        return dp[0][0]
        
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    str1 = "abac"
    str2 = "cab"
    
    print(solution.shortestCommonSupersequence(str1, str2))
    
    
    
## Above Solution gives MLE


## Below Solution works using directions

# class Solution:
#     def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
#         m, n = len(str1), len(str2)
#         # dp[r][c] will hold the length of the SCS for str1[c:] and str2[r:]
#         dp = [[0] * (m + 1) for _ in range(n + 1)]
#         # direction[r][c] will store the direction: 'D', 'H', or 'V'
#         direction = [[None] * (m + 1) for _ in range(n + 1)]
        
#         # Base cases:
#         # If str1 is empty, the answer is the remainder of str2.
#         for r in range(n, -1, -1):
#             dp[r][m] = n - r
#             direction[r][m] = 'V'  # Vertical move (choose str2)
#         # If str2 is empty, the answer is the remainder of str1.
#         for c in range(m, -1, -1):
#             dp[n][c] = m - c
#             direction[n][c] = 'H'  # Horizontal move (choose str1)
        
#         # Fill dp and direction table in reverse order.
#         for r in range(n - 1, -1, -1):
#             for c in range(m - 1, -1, -1):
#                 if str1[c] == str2[r]:
#                     # Characters match: use this character and move diagonally.
#                     dp[r][c] = 1 + dp[r + 1][c + 1]
#                     direction[r][c] = 'D'
#                 else:
#                     # Choose the option that gives a shorter supersequence.
#                     if dp[r][c + 1] < dp[r + 1][c]:
#                         dp[r][c] = 1 + dp[r][c + 1]
#                         direction[r][c] = 'H'
#                     else:
#                         dp[r][c] = 1 + dp[r + 1][c]
#                         direction[r][c] = 'V'
        
#         # Reconstruct the SCS from the direction table.
#         r, c = 0, 0
#         scs_chars = []
#         while r < n and c < m:
#             if direction[r][c] == 'D':
#                 scs_chars.append(str1[c])  # same as str2[r]
#                 r += 1
#                 c += 1
#             elif direction[r][c] == 'H':
#                 scs_chars.append(str1[c])
#                 c += 1
#             else:  # direction[r][c] == 'V'
#                 scs_chars.append(str2[r])
#                 r += 1
        
#         # Append any remaining characters.
#         if c < m:
#             scs_chars.append(str1[c:])
#         if r < n:
#             scs_chars.append(str2[r:])
        
#         return ''.join(scs_chars)

# # Example testing:
# if __name__ == "__main__":
#     solution = Solution()
#     str1 = "abac"
#     str2 = "cab"
#     print(solution.shortestCommonSupersequence(str1, str2))  # Expected: "cabac" or another valid SCS.
