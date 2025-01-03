from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import List, Optional
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    
    def __init__(self, node:ListNode):
        self.node = node
        
    def __lt__(self, node2:ListNode):
        return self.node.val < node2.node.val
    
    
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        final_linked_list = ListNode(0) 
        cur = final_linked_list
        minheap = []
        
        
        for listt in lists:
            # print(f"type of listt ::{type(listt)}")
            # print(f"listt ::{(listt)}")
            
            if listt is not None:
                wrapper_node = NodeWrapper(listt)
                heapq.heappush(minheap, wrapper_node)
                print(wrapper_node.node.val)
            
        print([x.node.val for x in minheap])


        while(minheap):
            wrapper_node = heapq.heappop(minheap)
            cur.next = wrapper_node.node
            cur = cur.next

            if wrapper_node.node.next:
                heapq.heappush(minheap, NodeWrapper(wrapper_node.node.next))

        return final_linked_list.next

        
        
def build_linked_list(values):
    """Convert a Python list into a linked list (ListNode)."""
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    """Print a linked list for verification."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

if __name__ == "__main__":
    solution = Solution()

    # Convert Python lists to linked lists
    lists = [
        build_linked_list([1, 4, 5]),
        build_linked_list([1, 3, 4]),
        build_linked_list([2, 6]),
    ]
    
    # Merge k sorted linked lists
    merged_list = solution.mergeKLists(lists=lists)

    # Print the result as a Python list
    print_linked_list(merged_list)