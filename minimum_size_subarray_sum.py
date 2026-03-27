class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    # method we are using is the sliding window method
        left=0
        right = 0
        current_sum = 0

        res = float('inf')
  
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                res = min(res, right - left + 1)
                current_sum -= nums[left]
                left += 1
            
        return 0 if res == float('inf') else res
# Time complexity is O(n) because we are traversing the array once with the right pointer and the left pointer will also traverse the array at most once.
# Space complexity is O(1) because we are using only a constant amount of extra space
        