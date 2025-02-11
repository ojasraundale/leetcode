from typing import List


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        def return_top_stack_reverse(ans, length):
            return "".join(ans[-length:])
        
        
        ans = []
        for c in s:
            ans.append(c)
            if len(ans) >= len(part):
                if c == part[-1]:
                    if return_top_stack_reverse(ans, len(part)) == part:
                        for _ in range(len(part)):
                            ans.pop()

        return "".join(ans)
    
    
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    s = "daabcbaabcbc"
    part = "abc"
    
    
    print(solution.removeOccurrences(s, part))