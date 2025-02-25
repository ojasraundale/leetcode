from typing import List


"""
[1,2,3,4,5,6,7]

dp_even:
[0,1,1,2,2]
dp_odd:
[1,1,2,2,3]
"""

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        print(arr)
        
        for i in range(len(arr)):
            arr[i] %= 2
            
        
        dp_even = [0 for _ in range(len(arr))]
        dp_odd = [0 for _ in range(len(arr))]
        
        
        if arr[0] == 0:
            dp_even[0] = 1
        else:
            dp_odd[0] = 1
            
        for i in range(1, len(arr)):
            if arr[i] == 0:
                dp_even[i] = 1 + dp_even[i-1]
                dp_odd[i] = dp_odd[i-1]
            
            else:
                dp_odd[i] = 1 + dp_even[i-1]  
                dp_even[i] = dp_odd[i-1]
        
        ans = 0
        for i in dp_odd:
            ans += i
            
        print(dp_odd)
        print(dp_even)
        return ans% (10**9 + 7)
    
        # dp = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]        
        
        # # print(dp)
        # ans = 0
        # for i in range(len(arr)):
        #     # dp[i][i] = arr[i] % 2
        #     # ans += dp[i][i]
        #     arr[i] % 2
        # print(dp)
        
        
        # for row in range(0, len(arr)):
        #     for col in range(row+1, len(arr)):
        #         print(row, col)
        #     # print()
                
        #         dp[row][col] = (dp[row][col-1] + arr[col] )%2
        #         ans+= dp[row][col]

        # print(dp)

        # return ans%(1000000007)
# Testing locally
if __name__ == "__main__":
    
    arr = [1,2,3,4,5,6,7]
    
    solution = Solution()
    
    print(solution.numOfSubarrays(arr=arr))