# Complexity Analysis
# Time Complexity: O(n)

# We iterate through the array twice: once forward to build the prefix products and once backward to apply the postfix products. Since these are sequential passes, it is linear time.

# Space Complexity: O(1) (Extra Space)

# The problem usually specifies that the output array does not count toward the space complexity. Aside from the result array, we only use a single integer variable (right_product), making the auxiliary space constant.

# Purpose: Why Use This?
# The goal is to find the product of all elements in an array except the one at the current index, without using the division operator.

# The "Division" Trap: A simple way would be to multiply everything and then divide by nums[i]. However, this breaks if there is a 0 in the array (division by zero) and is often forbidden in interviews to test your logic.

# Efficiency: This approach avoids the O(n 
# 2
#  ) "brute force" method (nested loops) which would be too slow for large datasets.

# Real-world Use: This pattern is common in functional programming and stream processing where you need to calculate "running" totals or context-aware values without re-scanning the entire dataset.
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        total_array = [1]*len(nums)
        product=0
        # Prefix:# Step 1: Calculate Prefix products
        # Each element at res[i] will contain the product of all numbers to the left of i
        for i in range(1,len(nums)):
            total_array[i] = total_array[i-1]*nums[i-1] 
        #postfix
        right_product = 1
        for j in range(len(nums) - 1, -1, -1):
           # 1. COMBINE: Multiply the left product (already in answer[i])     by the right product
           total_array[j] = total_array[j] * right_product
           
          # 2. UPDATE: Grow the right product by multiplying it by the current number
           right_product = right_product * nums[j]
        return total_array

def run_tests():
    sol = Solution()
    
    # Test Case 1: Standard positive integers
    nums1 = [1, 2, 3, 4]
    expected1 = [24, 12, 8, 6]
    assert sol.productExceptSelf(nums1) == expected1, f"Failed on {nums1}"
    
    # Test Case 2: Array with a single zero
    nums2 = [-1, 1, 0, -3, 3]
    expected2 = [0, 0, 9, 0, 0]
    assert sol.productExceptSelf(nums2) == expected2, f"Failed on {nums2}"
    
    # Test Case 3: Array with multiple zeros
    nums3 = [2, 3, 0, 0]
    expected3 = [0, 0, 0, 0]
    assert sol.productExceptSelf(nums3) == expected3, f"Failed on {nums3}"
    
    # Test Case 4: Minimum array size
    nums4 = [1, 5]
    expected4 = [5, 1]
    assert sol.productExceptSelf(nums4) == expected4, f"Failed on {nums4}"
    
    print("All test cases passed successfully!")

if __name__ == "__main__":
    run_tests()