from typing import List

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         print(nums)
#         triplets = []
        
#         i = 0
#         while i < len(nums) - 2:
#             if i > 0 and nums[i-1] == nums[i]:
#                 i+=1
#                 continue
            
#             target = -nums[i]
#             print(target)
#             j = i+1
#             k = len(nums) - 1
#             print(i,j,k)    
#             while j < k :
#                 # print(j,k)
#                 # print(f"nums[j], nums[k], target : {nums[j], nums[k], target}")
#                 while j+1 < k and nums[j+1] == nums[j]:
#                         j+=1
#                 while j < k-1 and nums[k-1] == nums[k]: 
#                         k-=1
#                 if nums[j] + nums[k] == target:
#                     print("in 1 if")
#                     triplets.append([nums[i],nums[j],nums[k]])
#                     j+=1
#                     k-=1
                    
                
#                 elif nums[j] + nums[k] < target:
#                     # print("in 2 if")
#                     j+=1
#                     # print(j+1 < k)
#                     # print(nums[j+1] == nums[j])
#                     # while j+1 < k and nums[j+1] == nums[j]:
#                     #     print("2 while met")
#                     #     j+=1
                        
#                 elif nums[j] + nums[k] > target:
#                     # print("in 3 if")
#                     k-=1
#                     # while j < k-1 and nums[k-1] == nums[k]: 
#                     #     k-=1       
            
#             i+=1
            
#         return triplets
        
        
#         # while j < k :
#         #         print(j,k)
#         #         print(f"nums[j], nums[k], target : {nums[j], nums[k], target}")
#         #         if nums[j] + nums[k] == target:
#         #             print("in 1 if")
#         #             triplets.append([nums[i],nums[j],nums[k]])
#         #             j+=1
#         #             k-=1
#         #             while j+1 < k and nums[j+1] == nums[j]:
#         #                 j+=1
#         #             while j < k-1 and nums[k-1] == nums[k]: 
#         #                 k-=1
                
#         #         elif nums[j] + nums[k] < target:
#         #             print("in 2 if")
#         #             j+=1
#         #             print(j+1 < k)
#         #             # print(nums[j+1] == nums[j])
#         #             while j+1 < k and nums[j+1] == nums[j]:
#         #                 print("2 while met")
#         #                 j+=1
                        
#         #         elif nums[j] + nums[k] > target:
#         #             print("in 3 if")
#         #             k-=1
#         #             while j < k-1 and nums[k-1] == nums[k]: 
#         #                 k-=1       
            
#         #     i+=1
            
#         # return triplets
            
        
        
#         ## TLE for just 1 test case out of 313. 
        
#         # targets = [-nums[i] for i in range(len(nums))]
#         # # print(targets)
        
#         # triplets = set()  
#         # for i,target in enumerate(targets):
#         #     hashmap = {}
#         #     for j in range(i+1, len(nums)):
#         #         if target - nums[j] in hashmap:
#         #             # print(target)
#         #             k = hashmap[target - nums[j]]
#         #             # print(i, j, k)
#         #             if j != i and i!=k and j!=k :
#         #                 # print(i, j, k)
#         #                 tri = [nums[i], nums[j], nums[k]]
#         #                 tri.sort()
#         #                 # if tri not in triplets:
#         #                 triplets.add(tuple(tri))
#         #         hashmap[nums[j]] = j
                 
        
#         # # return list(set(triplets))
#         # return [list(x) for x in triplets]
        
        
#         # print(nums)
        
#         # nums.sort()
        
#         # non_repeat = [nums[0]]
        
#         # for i in range(1, len(nums)):
#         #     if nums[i] == nums[i-1]:
#         #         continue
#         #     non_repeat.append(nums[i])
        
#         # # print(nums)
#         # # print(non_repeat)
        
#         # nums = non_repeat
            
#         # targets = [-nums[i] for i in range(len(nums))]
#         # print(targets)
        
#         # triplets = []
#         # # triplets = {}
#         # for i,target in enumerate(targets):
#         #     hashmap = {}
#         #     for j in range(i+1, len(nums)):
#         #         if target - nums[j] in hashmap:
#         #             # print(target)
#         #             k = hashmap[target - nums[j]]
#         #             print(i, j, k)
#         #             if j != i and i!=k and j!=k :
#         #                 print(i, j, k)
#         #                 tri = [nums[i], nums[j], nums[k]]
#         #                 tri.sort()
#         #                 # if tri not in triplets:
#         #                 #     triplets.append(tri)
#         #                 triplets.append(tri)
#         #                 # triplets[tri] = 1
#         #         hashmap[nums[j]] = j
                
        
        
#         # # return list(set(triplets))
#         # # return list[triplets.keys()]
#         # return triplets
                
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        
        i = 0
        while i < len(nums) - 2:
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
            
            i += 1
        
        return triplets
        
        
        
# Testing locally
if __name__ == "__main__":        
    nums = [-1,0,1,2,-1,-4]
    nums = [-2,0,0,2,2]
    # [-4, -1, -1, 0, 1, 2]
    solution = Solution()
    print(solution.threeSum(nums=nums))
    