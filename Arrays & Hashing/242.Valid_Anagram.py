class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

sol_242 = Solution()

# Test cases for 242. Valid Anagram
print(sol_242.isAnagram("anagram", "nagaram"))  # Expected: True
print(sol_242.isAnagram("rat", "car"))          # Expected: False
print(sol_242.isAnagram("a", "a"))              # Expected: True
print(sol_242.isAnagram("a", "ab"))             # Expected: False
