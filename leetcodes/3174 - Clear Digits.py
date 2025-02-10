from typing import List

class Solution:
    def clearDigits(self, s: str) -> str:
        print(s)
        
        print(ord(str(0)))
        stack = []
        for c in s:
            print(c, ord(c))
            if 48<=ord(c)<58:
                stack.pop()
            else:
                stack.append(c)
        print(stack)
        # ans = ""
        
        ans = "".join(stack)
        
        print(ans)  
        return(ans)
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    s = "cb34"
    
    print(solution.clearDigits(s=s))