from typing import Optional, List


class Solution:
    def helper(self, nums: List[int]) -> int:
        ans = [0 for i in range(len(nums))]
        # not_using = [0 for i in range(len(nums))]

        ans[0] = nums[0]

        if len(nums) == 1:
            return ans[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        ans[1] = max(ans[0], nums[1])

        for i in range(2, len(nums)):
            ans[i] = max(ans[i-2]+nums[i], ans[i-1])

        return ans[len(nums)-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(
            self.helper(nums=nums[0:-1]),
            self.helper(nums=nums[1:])
                   )


# Testing locally
if __name__ == "__main__":
    
    solution = Solution()
    
    nums = [1,2,3,1]
    print(solution.rob(nums=nums))