from typing import List
import heapq

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        print(limit)
        
        color_dict = {}     # no. of times color used 
        ball_dict = {}      # ball to current color 
        
        current_distinct = 0
        
        ans = []
        
        for ball,color in queries:
            print(f"ball,color: {ball,color}")
            
            # untouched ball
            current_color = ball_dict.get(ball, -1)
            if current_color == -1:
                ball_dict[ball] = color
                
                if color_dict.get(color, 0) == 0:
                    current_distinct += 1
                color_dict[color] = 1 + color_dict.get(color, 0)
            
            # touched ball 
            else:
                ball_dict[ball] = color
                current_color_count = color_dict.get(current_color, 0)
                if current_color_count == 0:
                    print("wtf?")

                color_dict[current_color] = current_color_count - 1
                
                if color_dict[current_color] == 0:
                    current_distinct -= 1
                
                color_count = color_dict.get(color, 0)
                if color_count == 0:
                    current_distinct += 1
                
                color_dict[color] = 1 + color_count
                
            ans.append(current_distinct)
            
            print(f"color_dict = {color_dict}")   
            print(f"ball_dict = {ball_dict}")   
            print(f"current_distinct = {current_distinct}")
            print()
        print(ans)
        return ans
    
    
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    limit = 4
    queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
    
    
    print(solution.queryResults(limit, queries))