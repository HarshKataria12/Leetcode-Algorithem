class Solution:
  def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    res = nums[0] + nums[1] + nums[2]
    minimum = float('inf')
    n = len(nums)

    for i in range(n-2):
        left = i + 1
        right = n - 1

        while left < right:
            s = nums[i] + nums[left] + nums[right]

            if abs(s - target) < minimum:
                    res = s
                    minimum = abs(s - target)
            if s == target:
                return s
            elif s < target:
                left += 1
            else:                
               right -= 1
    return res