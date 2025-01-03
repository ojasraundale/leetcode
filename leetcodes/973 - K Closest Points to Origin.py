from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        k_counter = 0
        for point in points:
            
            sq_dist = point[0]**2 + point[1]**2
            heapq.heappush(heap, (sq_dist, point))
            k_counter += 1
        
        ans = []
        
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])     
            # print(point)
            # print()
        
        return ans
        
            
        
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    points = [[1,3],[-2,2]]
    k = 1
    print(solution.kClosest(points=points, k=k))
    