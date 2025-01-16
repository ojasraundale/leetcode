from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        print(A, B)
        
        freq = [0]*100
        
        ans = []
        counter = 0
        for a,b in zip(A, B):
            freq[a]+=1
            freq[b]+=1
            if freq[a] == 2:
                counter+=1
            if freq[b] == 2:
                counter+=1
            if a==b:
                counter-=1
            ans.append(counter)                            
        
        return ans
            
        
# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    A = [1,3,2,4]
    B = [3,1,2,4]
    
    print(solution.findThePrefixCommonArray(A=A, B=B))