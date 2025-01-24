from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # print(graph)
        
        node_status = [0]*len(graph)
        # 0 = not visited
        # 1 = in stack
        # 2 = safe / visited
        # 3 = unsafe
        
        # print(node_status)
        
        
        def is_safe(graph, node_status, node):
            # Leaf node
            # print(f"node, graph[node] : {node, graph[node]}")
            if len(graph[node]) == 0:
                node_status[node] = 2
                return True
            
            if node_status[node] == 2:
                return True
            # print(node_status)
            
            if node_status[node] == 1 or node_status[node] == 3:
                node_status[node] = 3
                return False

            if node_status[node] == 0:
                # print("Node status = 1, DFSing")
                node_status[node] = 1
                children_safe = True
                for neighbour in graph[node]:
                    neighbour_safe = is_safe(graph, node_status, neighbour)
                    children_safe = children_safe and neighbour_safe
                    
                if children_safe:
                    node_status[node] = 2
                    return True
                else:
                    node_status[node] = 3
                    return False
                
        for node in range(len(graph)):
            is_safe(graph, node_status, node)
        
        ans = []
        for node in range(len(graph)):
            if node_status[node] == 2:
                ans.append(node)
            
        return ans
            
                    
                    
        
    
# Testing locally
if __name__ == "__main__":        
    
    # graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    graph = [[],[0,2,3,4],[3],[4],[]]
    
    solution = Solution()
    
    print(solution.eventualSafeNodes(graph))