# # Group Anagrams

# LeetCode problem: Group Anagrams

# ## Approach
# - Sort each word
# - Use sorted word as dictionary key
# - Store words with same key in list
# - Return dictionary values

# ## Time Complexity
# O(n * k log k)

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = {}
    
        for word in strs:
            # Sort the word to get the anagram key
            sorted_word = ''.join(sorted(word))
        
            # Add the original word to the corresponding anagram group
            if sorted_word in anagram_map:
                anagram_map[sorted_word].append(word)
            else:
                anagram_map[sorted_word] = [word]
    
        # Return the list of anagram groups
        return list(anagram_map.values())


# 🔹 Create object of class
solution = Solution()

# 🔹 Test Case 1
test1 = ["eat","tea","tan","ate","nat","bat"]
print("Test Case 1 Input:", test1)
print("Output:", solution.groupAnagrams(test1))
print()

# 🔹 Test Case 2
test2 = ["listen","silent","enlist","hello","ohlle"]
print("Test Case 2 Input:", test2)
print("Output:", solution.groupAnagrams(test2))
print()

# 🔹 Test Case 3 (single word)
test3 = ["python"]
print("Test Case 3 Input:", test3)
print("Output:", solution.groupAnagrams(test3))
print()

# 🔹 Test Case 4 (empty list)
test4 = []
print("Test Case 4 Input:", test4)
print("Output:", solution.groupAnagrams(test4))
print()

# 🔹 Test Case 5 (many small words)
test5 = ["ab","ba","abc","cab","bca","xy","yx"]
print("Test Case 5 Input:", test5)
print("Output:", solution.groupAnagrams(test5))
