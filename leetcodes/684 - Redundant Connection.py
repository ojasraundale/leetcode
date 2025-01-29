from typing import List
from collections import deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        print(edges)
        
        
        adjList = {i:[] for i in range(1,len(edges)+1)}
        Degrees = [0 for _ in range(1, len(edges)+1)]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
            Degrees[edge[0]-1] += 1
            Degrees[edge[1]-1] += 1
        
        print(adjList)
        print(Degrees)
        
        q = deque()
        
        for node in range(1, len(edges)+1):
            if Degrees[node-1] == 1:
                q.append(node)
                
        print(q)
        while q:
            node = q.popleft()
            Degrees[node-1] -= 1
            
            neighbour = adjList[node][0]
            Degrees[neighbour-1] -= 1
            
            adjList[node].remove(neighbour)
            adjList[neighbour].remove(node)
            
            if Degrees[neighbour-1] == 1:
                q.append(neighbour)
                
        print(adjList)
        print(Degrees)
        
        ans = None
        for edge in edges:
            if Degrees[edge[0]-1] == Degrees[edge[1]-1] and Degrees[edge[1]-1] == 2:
                print(edge)
                ans = edge
        
        print("AnS:")
        
        return ans
            
            
            
        
# Testing locally
if __name__ == "__main__":          
    
    solution = Solution()
    
    edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    
    print(solution.findRedundantConnection(edges))