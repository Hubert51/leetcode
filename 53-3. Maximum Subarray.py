#  这题我的思路不好，不应该用0作为比较基准，因为没有办法处理负数。用greedy algorithm

# first approach
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         if max(nums) <= 0:
#             largestSum = max(nums)
#         else:
#             largestSum = 0
#         currentSum = 0
#         for num in nums:
#             if currentSum + num <= 0:
#                 currentSum = 0
#                 continue
#             else:
#                 currentSum += num
#                 if currentSum >= largestSum:
#                     largestSum = currentSum      
#         return largestSum
    
# greedy approach:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = maxSum = nums[0]
        
        for index in range(1,len(nums)):
            curSum = max(nums[index], curSum+nums[index])
            maxSum = max(curSum, maxSum)
            
        return maxSum

