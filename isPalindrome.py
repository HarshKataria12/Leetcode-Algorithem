class Solution:
    def isPalindrome(self, s: str) -> bool:
        case_character = ''.join([char for char in s if char.isalnum()]).lower()
        
        if len(case_character) <= 1:
            return True
        
        mid = len(case_character) // 2
        
        if len(case_character) % 2 == 0:
            left = case_character[:mid]
            right = case_character[mid:]
        else:
            left = case_character[:mid]
            right = case_character[mid+1:]
        
        return left == right[::-1]


def run_tests():
    sol = Solution()
    
    tests = [
        ("", True),
        ("a", True),
        ("aa", True),
        ("aba", True),
        ("abba", True),
        ("racecar", True),
        ("A man, a plan, a canal: Panama", True),
        ("No lemon, no melon", True),
        ("Was it a car or a cat I saw?", True),
        ("hello", False),
        ("race a car", False),
        ("0P", False),
        ("ab", False),
        ("12321", True),
        ("123321", True),
        ("12345", False),
    ]
    
    for s, expected in tests:
        result = sol.isPalindrome(s)
        print(f"Input: {s!r:30} | Expected: {expected} | Got: {result}")

run_tests()