class Solution(object):
    def isPalindrome(self, s):
        valid_pal = "".join(c.lower() for c in s if c.isalnum())

        return valid_pal == valid_pal[::-1]

sol = Solution()
# Test cases for Valid Palindrome
print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # Expected: True
print(sol.isPalindrome("race a car"))                      # Expected: False
print(sol.isPalindrome(""))                                # Expected: True
print(sol.isPalindrome(" "))                               # Expected: True
print(sol.isPalindrome("ab_a"))                            # Expected: True