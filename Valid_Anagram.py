# Short Summary
# The algorithm checks whether two strings are anagrams by:
# First verifying both strings have the same length.
# Counting how many times each character appears in string t.
# Iterating through string s and decreasing counts.
# If any character is missing or overused → return False.
# If all counts match → return True.

# Time & Space Complexity
# Time Complexity: O(n)
# We traverse both strings once.
# Space Complexity: O(k)
# Where k = number of unique characters (max 26 for lowercase letters).
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Dictionary to store frequency of characters from string t
        char_frequency = {}
        
        # If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Count characters in string t
        for char in t:
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1
        
        # Check characters in string s against the frequency map
        for char in s:
            # If char not found OR used more times than available → not anagram
            if char not in char_frequency or char_frequency[char] <= 0:
                return False
            
            # Reduce frequency since this character is matched
            char_frequency[char] -= 1
        
        # If all characters matched, strings are anagrams
        return True
    

print(Solution().isAnagram("anagram", "nagaram"))   # True
print(Solution().isAnagram("listen", "silent"))     # True
print(Solution().isAnagram("triangle", "integral")) # True
print(Solution().isAnagram("evil", "vile"))         # True
print(Solution().isAnagram("aabbcc", "abcabc"))     # True

print(Solution().isAnagram("aacc", "ccac"))       # False
print(Solution().isAnagram("hello", "world"))   # False
print(Solution().isAnagram("aabb", "ab"))       # False
print(Solution().isAnagram("test", "ttew"))     # False
print(Solution().isAnagram("", ""))   # True
print(Solution().isAnagram("a", ""))  # False

