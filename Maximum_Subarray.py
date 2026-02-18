# Problem:
# Find the maximum sum of a contiguous subarray.
# Idea:
# At every number we decide:
# Continue the previous subarray
# OR start a new subarray here
# We keep two variables:
# current_sum → best subarray ending at current index
# max_sum → best subarray found so far



class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > current_sum + nums[i]:
                current_sum = nums[i]      # restart
            else:
                current_sum = current_sum + nums[i]   # continue

            if current_sum > max_sum:
                max_sum = current_sum 
        return max_sum
    
#     Approach type:
# Greedy + Dynamic Programming (Kadane’s Algorithm)
# Time Complexity: O(n)
# Space Complexity: O(1)

# create object of solution
sol = Solution()

tests = [
    ([-2,1,-3,4,-1,2,1,-5,4], 6),
    ([5,4,-1,7,8], 23),
    ([-3,-2,-5,-1], -1),
    ([7], 7),
    ([1,-2,3,5,-1,2], 9)
]

for nums, expected in tests:
    result = sol.maxSubArray(nums)
    print("Input:", nums)
    print("Output:", result)
    print("Expected:", expected)
    print("Pass:", result == expected)
    print("-----")
