class Solution(object):
    def isPalindrome(self, s):
        valid_pal = "".join(c.lower() for c in s if c.isalnum())

        return valid_pal == valid_pal[::-1]

sol_125 = Solution()

# Test cases for 125. Valid Palindrome
print(sol_125.isPalindrome("A man, a plan, a canal: Panama"))  # Expected: True
print(sol_125.isPalindrome("race a car"))                      # Expected: False
print(sol_125.isPalindrome(""))                                # Expected: True
print(sol_125.isPalindrome(" "))                               # Expected: True
print(sol_125.isPalindrome("ab_a"))                            # Expected: True
