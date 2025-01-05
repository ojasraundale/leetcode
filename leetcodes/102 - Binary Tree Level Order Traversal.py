from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        print(root.val)
        
        q = deque()
        q.append(root)
        
        res = []
        while(q):
            level = []
            lenQ = len(q)
            # print(q)
            
            for i in range(lenQ):
                node:TreeNode = q.popleft()
                # print(node)
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if level:
                # print(level)
                res.append(level)
                
        return res
        

if __name__ == "__main__":
    # Construct the binary tree: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    solution = Solution()
    print(solution.levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]