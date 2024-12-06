class Solution(object):
    def containsDuplicate(self, nums):
        set_num = set()
        for num in nums:
            if num in set_num:
                return True
            set_num.add(num)
        return False

s = Solution()
# Test cases for Contains Duplicate
print(s.containsDuplicate([1, 2, 3, 1]))  # Expected: True
print(s.containsDuplicate([1, 2, 3, 4]))  # Expected: False
print(s.containsDuplicate([1, 1, 1, 1]))  # Expected: True
print(s.containsDuplicate([]))            # Expected: False