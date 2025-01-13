
class Solution:
    def minimumLength(self, s: str) -> int:
        '''
            "aaaaa" -> 1
            
            "aaaa" -> 2
            
            "aaaaaa" -> 2
            
            
            3>1
            4>2
            5>1
        '''
        
        string_hash = [0]*26
        

        for c in s:
            string_hash[ord(c)-ord('a')]+=1
            
        res = 0
            
        for c in string_hash:
            if c > 0:
                if c%2 == 0:
                    res+=2
                else:
                    res+=1
                    
                
        return res    
    
# Testing locally
if __name__ == "__main__":
    
    s = "abaacbcbb"
    
    solution = Solution()
    print(solution.minimumLength(s=s))