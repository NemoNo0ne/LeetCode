class Solution(object):
    def containsDuplicate(self, nums):
        set_num = set()
        for num in nums:
            if num in set_num:
                return True
            set_num.add(num)
        return False

sol_217 = Solution()

# Test cases for 217. Contains Duplicate
print(sol_217.containsDuplicate([1, 2, 3, 1]))  # Expected: True
print(sol_217.containsDuplicate([1, 2, 3, 4]))  # Expected: False
print(sol_217.containsDuplicate([1]))           # Expected: False
print(sol_217.containsDuplicate([]))            # Expected: False
