from typing import List
from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        print(numCourses)
        
        inDegree = [0] * numCourses
        
        adjlist = {c1:[] for c1 in range(numCourses)}
        
        # print(inDegree)
        for c1, c2 in prerequisites:
            # print(c1, c2)
            inDegree[c2] += 1
            adjlist[c1].append(c2)
        print(inDegree)
        print(adjlist)

        
        q = deque()
        
        for c1, degree in enumerate(inDegree):
            if degree == 0:
                q.appendleft(c1)
                
        print(q)
        
        all_req = {c1: set() for c1 in range(numCourses)}
        
        print(all_req)
        while q:
            current_course = q.popleft()
            
            for next_course in adjlist[current_course]:
                print(f"current_course, next_course = {current_course, next_course}")
                all_req[next_course].add(current_course)
                all_req[next_course] = all_req[next_course].union(all_req[current_course])
                inDegree[next_course] -= 1
                if inDegree[next_course] == 0:
                    q.append(next_course)

                print(all_req)
            print(f"inDegree after {current_course}: {inDegree}")
                    
        print(all_req)
        
        ans = []
        for query in queries:
            c1 = query[0]
            c2 = query[1]
            
            if c1 in all_req[c2]:
                ans.append(True)
            else:
                ans.append(False)
                
        return ans
            
            
            
                
            
        
# Testing locally
if __name__ == "__main__":        
    
    solution = Solution()
    
    numCourses = 5
    prerequisites = [[0,1],[1,2],[2,3],[3,4]]
    queries = [[0,4],[4,0],[1,3],[3,0]]
    
    # numCourses = 3
    # prerequisites = [[1,2],[1,0],[2,0]]
    # queries = [[1,0],[1,2]]
    
    
    
    print(solution.checkIfPrerequisite(numCourses, prerequisites, queries))