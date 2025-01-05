from collections import deque
from typing import Optional, List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        print(s, shifts)
        
        # for i, (start, end, direction) in  enumerate(shifts):
            
        #     print(i, s[i], ord(s[i])-ord('a'), start, end, direction)
            
        #     char_og = ord(s[i])-ord('a')
            
        #     # if direction == 0:
                
        #     # else:
        shift_agg_array = [0 for i in range(len(s)+1)]
        res = ''
        
        
        for i, (start, end, direction) in enumerate(shifts):
            if direction == 1:
                shift_agg_array[start]+= 1
                shift_agg_array[end+1]-= 1
            else:
                shift_agg_array[start]-= 1
                shift_agg_array[end+1]+= 1
                
            print(shift_agg_array)
        
        shift = 0        
        
        print(f"shift_agg_array = {shift_agg_array}")
        for i,c in enumerate(s):
            shift+= shift_agg_array[i]
            char_og = ord(s[i])-ord('a')  
            new_char_diff = (char_og + shift) % 26  
            res = res + (chr(ord('a') + new_char_diff))
        
        return res
    
# Testing locally
if __name__ == "__main__":
    
    # print(-1%26)
    solution = Solution()
    s = "abc"
    shifts = [[0,1,0],[1,2,1],[0,2,1]]        
    
    print(solution.shiftingLetters(s=s, shifts=shifts))    
        
