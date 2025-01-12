from typing import List

class Solution:
    # def canBeValid(self, s: str, locked: str) -> bool:
    #     print(s, locked)    
        
    #     res = True
    #     if len(s)%2 == 1:
    #         return False
         
    #     stack = []
        
    #     ####
    #     '''
    #     greedy
    #     cases: 
    #     (, 0, push
    #     (, 1, push into stack directly
    #     ), 0, pop but check previous -> if previous (, 1 then pop both
    #                                                 (, 0 then pop both
    #                                                 ), 1 then return False
    #                                                 ), 0 then pop both
        
    #     ), 1, pop but check previous -> if previous (, 1 then pop both
    #                                                 (, 0 then pop both
    #                                                 ), 1 then return False
    #                                                 ), 0 then pop both
        
    #     '''
        
    #     for para, lock in zip(s,locked):
    #         print(f"stack = {stack}")   
    #         # print(para, lock)
    #         if para == '(':
    #             if not stack:
    #                 stack.append((para, lock))
    #                 continue
    #             else:
    #                 if lock == '0':
    #                     para_prev, lock_prev = stack.pop()
    #                     if lock_prev == '0':
    #                         continue
    #                     else:
    #                         if para_prev == '(':
    #                             continue
    #                         else:
    #                             return False
    #                 else:
    #                     stack.append((para, lock))
                        
                    
                
    #         else:
    #             if not stack:
    #                 stack.append((para, lock))
    #                 continue
    #             para_prev, lock_prev = stack.pop()
    #             if lock_prev == '0':
    #                 continue
    #             else:
    #                 if para_prev == '(':
    #                     continue
    #                 else:
    #                     return False
                
    #     if len(stack) > 0: 
    #         return False
        
    #     return True
                    
                
    def canBeValid(self, s, locked):
        length = len(s)

        # If length of string is odd, return false.
        if length % 2 == 1:
            return False

        open_brackets = []
        unlocked = []

        # Iterate through the string to handle '(' and ')'
        for i in range(length):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                open_brackets.append(i)
            elif s[i] == ")":
                if open_brackets:
                    open_brackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        # Match remaining open brackets and the unlocked characters
        while open_brackets and unlocked and open_brackets[-1] < unlocked[-1]:
            open_brackets.pop()
            unlocked.pop()

        if open_brackets:
            return False

        return True                
                
                
                        
            
            
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    # s = "()()"
    # s = "))()))"
    # s = ")("
    s = "(()())"
    
    
    # locked = "0000"
    # locked = "010100"
    # locked = "00"
    locked = "111111"
    
    print(solution.canBeValid(s=s,locked=locked))