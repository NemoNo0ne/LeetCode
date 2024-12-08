class Solution(object):
    def isValid(self, s):
        brakets = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in brakets:
                top_element = stack.pop() if stack else '$'
                if brakets[char] != top_element:
                    return False
            else:
                stack.append(char)

        return True if len(stack) == 0 else False


sol_20 = Solution()

# Test cases for 20. Valid Parentheses
print(sol_20.isValid("()"))          # Expected: True
print(sol_20.isValid("()[]{}"))      # Expected: True
print(sol_20.isValid("(]"))          # Expected: False
print(sol_20.isValid("([)]"))        # Expected: False
print(sol_20.isValid("{[]}"))        # Expected: True
print(sol_20.isValid(""))            # Expected: True