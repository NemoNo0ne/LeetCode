class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

sol = Solution()
# Test cases for Valid Anagram
print(sol.isAnagram("anagram", "nagaram"))  # Expected: True
print(sol.isAnagram("rat", "car"))          # Expected: False
print(sol.isAnagram("", ""))                # Expected: True
print(sol.isAnagram("a", "ab"))             # Expected: False