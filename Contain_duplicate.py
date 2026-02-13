#The algorithm converts the list into a set and compares its length with the original list. 
#Since inserting elements into a set requires iterating through the entire list, the time complexity is O(n). 
#The space complexity is O(n) because an additional set storing up to n elements is created.
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
    
# manual testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,1]))  # True
    print(sol.containsDuplicate([1]))  # False
