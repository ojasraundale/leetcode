from typing import List
import heapq

class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c =="-":
                stack.append(stack.pop() - stack.pop())
            elif c =="/":
                stack.append(int(stack.pop() / stack.pop()))
            elif c =="*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(c))
            
            print(stack)
            
        return stack[0]        
            
        
        
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    tokens = ["2","1","+","3","*"]
    
    print(solution.evalRPN(tokens=tokens))