# <!-- User Engagement & Gamification (Streaks): Applications like Duolingo, fitness trackers (Strava), or Snapchat track daily usage. If you have a database of timestamps representing the days a user logged in, this algorithm can quickly determine their longest "daily streak" of continuous activity.

# Server Uptime & Network Logging:
# In DevOps, you might have logs of heartbeats or timestamps when a server was active. This logic can process millions of unsorted timestamp logs to find the longest continuous period (e.g., consecutive hours or days) a server stayed online without crashing. -->

def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0
    # I removed the print statements for cleaner test outputs, 
    # but the core logic remains exactly as you wrote it!
    for n in num_set:
        if (n - 1) not in num_set:
            length = 0
            while (n + length) in num_set:
                length += 1
            longest = max(length, longest)
    return longest

def run_tests():
    # 1. Standard Case: Random order
    assert longestConsecutive([100, 4, 200, 1, 3, 2]) == 4, "Failed: Standard Case" # Sequence: 1, 2, 3, 4
    
    # 2. Case with Duplicates: Set should filter these out naturally
    assert longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9, "Failed: Duplicates" # Sequence: 0-8
    
    # 3. Empty List: Should return 0
    assert longestConsecutive([]) == 0, "Failed: Empty List"
    
    # 4. Single Element: Should return 1
    assert longestConsecutive([5]) == 1, "Failed: Single Element"
    
    # 5. All Same Elements: Should return 1
    assert longestConsecutive([2, 2, 2, 2]) == 1, "Failed: All Same Elements"
    
    # 6. Negative Numbers: Should handle crossing 0
    assert longestConsecutive([0, -1, -2, -3, 5, 6]) == 4, "Failed: Negative Numbers" # Sequence: -3, -2, -1, 0
    
    # 7. No Consecutive Elements
    assert longestConsecutive([10, 20, 30, 40]) == 1, "Failed: No Consecutive Elements"

    print("All test cases passed successfully!")

run_tests()