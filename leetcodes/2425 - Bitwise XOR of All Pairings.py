from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        print(nums1, nums2)

        l1 = len(nums1)
        l2 = len(nums2)
        
        freq = {}
        
        for i in nums1:
            freq[i] = freq.get(i, 0) + l2
        
        for i in nums2:
            freq[i] = freq.get(i, 0) + l1
            
        ans = 0
        
        for i in freq:
            if freq[i]%2 == 1:
                ans = ans ^ i

        return ans
      
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    nums1 = [2,1,3]
    nums2 = [10,2,5,0]
    
    print(solution.xorAllNums(nums1=nums1, nums2=nums2))