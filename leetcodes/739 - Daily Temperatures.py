from typing import List, Optional

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # print(temperatures)
        stack = []
        
        result = [0]*len(temperatures)
        
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((i, temp))
            else:
                top_i, top_temp = stack[-1]
                while top_temp < temp:
                    result[top_i] = i-top_i
                    stack.pop()
                    if stack:
                        top_i, top_temp = stack[-1]
                    else:
                        break
                
                stack.append((i, temp))
        # print(result)
        return result
                
        
        
if __name__ == "__main__":
    solution = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    
    print(solution.dailyTemperatures(temperatures))
        
        
        