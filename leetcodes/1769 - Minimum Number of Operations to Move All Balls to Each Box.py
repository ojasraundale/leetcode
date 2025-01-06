from typing import Optional, List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        print(boxes)
        
        left_sum = 0
        left_n = 0
        right_sum = 0
        right_n = 0
        
        for i,b in enumerate(boxes):
            # print(i,b)
            # if i==0:
            #     pass
            if b == '1':
                right_n+=1
                right_sum+=i
        
        print(right_sum, right_n)
        
        res = []
        
        for i,b in enumerate(boxes):
            
            if b=='1':
                right_n-=1
                # right_sum-=1
                print(f"1:l+r:{left_sum, right_sum}")
                res.append(right_sum+left_sum)
                
                left_n+=1
                left_sum+=left_n
                right_sum-=right_n
                
            else:
                print(f"2:l+r:{left_sum, right_sum}")
                
                res.append(right_sum+left_sum)
                # left_n+=1
                left_sum+=left_n
                right_sum-=right_n
        
        return res
                
            
        
        
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    # boxes = "110"
    boxes = "001011"
    
    print(solution.minOperations(boxes=boxes))