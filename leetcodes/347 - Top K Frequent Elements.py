from typing import List
import heapq

class Solution:
    
    ## HashMap
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     hashmap = {}
    #     for i in nums:
    #         hashmap[i] = hashmap.get(i,0)+1
    #     print(hashmap)

    #     anss = []
    #     for KEY,VALUE in sorted(hashmap.items(), key = lambda x:x[1], reverse=True):
    #         anss.append((KEY, VALUE))
            
    #     return [anss[i][0] for i in range(k)]
    
    
    
    ## HeapQ 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            
            print(f"Heap = {heap}")
            if len(heap) > k:
                heapq.heappop(heap)
                print(f"Heap after pop = {heap}")


        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
            
        
            
        
# Testing locally
if __name__ == "__main__":
    # Test cases
    # test_cases = [
    #     ([1, 1, 1, 2, 2, 3], 2),  # nums, k
    #     ([1], 1),
    #     ([4, 4, 4, 6, 6, 6, 7], 1)
    # ]

    # for nums, k in test_cases:
    #     solution = Solution()
    #     print(f"Input: nums={nums}, k={k}")
    #     print(f"Output: {solution.topKFrequent(nums, k)}")        
    
    solution = Solution()
    
    nums = [1,1,1,2,2,3] 
    k = 2
    print(solution.topKFrequent(nums=nums, k=k))
    
    