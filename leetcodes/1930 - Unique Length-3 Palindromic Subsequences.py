

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left_charac = {}
        right_charac = {}

        res_dict = {}
        
        for c in s:
            right_charac[c] = right_charac.get(c, 0) + 1
            
        print(right_charac)
        
        lower_alpha = [chr(ord('a') + x) for x in range(26)]
        
        # print(lower_alpha)
        for m in s:
            right_charac[m] = right_charac.get(m,0) - 1
            
            for edge_char in lower_alpha:
                print(edge_char, m, left_charac, right_charac)
                
                if left_charac.get(edge_char,0) > 0 and right_charac.get(edge_char,0) > 0:
                    print(f"IN IFF saving {edge_char + m + edge_char}")
                    # print(edge_char + m + edge_char)
                    res_dict[edge_char + m + edge_char] = res_dict.get(edge_char + m + edge_char, 0) + 1
                    
                
            
            left_charac[m] = left_charac.get(m,0) + 1
            
            
            
        print(res_dict)
        print(len(res_dict))
        return(len(res_dict))
        
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    # s = "bbcbaba"
    s = "aabca"
    
    print(solution.countPalindromicSubsequence(s=s))
    