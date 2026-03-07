class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        maxFreq = 0
        res = 0

        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1
            maxFreq = max(maxFreq, count[ord(s[right]) - ord('A')])

            while (right - left + 1) - maxFreq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res