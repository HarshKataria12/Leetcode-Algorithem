
class Solution:
    # This approach is called:
# Brute Force / Exhaustive Search
# You try every possible pair until you find the answer.
# Time:  O(n²)
# Space: O(1)
    def twoSum(self,nums: list[int], target: int)-> list[int]:

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
# Best way is Instead of checking all pairs, we ask:
# “Have we already seen the number that would complete the target?”
# We store numbers in a dictionary so lookup is instant (O(1)).

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}   # number -> index

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []
                


if __name__ == "__main__":
    sol = Solution()

    print(sol.twoSum([2,7,11,15], 9))     # [0,1]
    print(sol.twoSum([1,3,4,2], 6))       # [2,3]
    print(sol.twoSum([-3,4,3,90], 0))     # [0,2]
    print(sol.twoSum([3,3], 6))           # [0,1]
    print(sol.twoSum([0,4,3,0], 0))       # [0,3]
    print(sol.twoSum([1,2,3,4,8], 12))    # [3,4]
    print(sol.twoSum([1,2,3], 100))       # []

    