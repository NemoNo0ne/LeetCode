class Solution(object):
    def twoSum(self, nums, target):
        num_hash = {}
        for idn, num in enumerate(nums):
            result = target - num
            if result in num_hash:
                return [num_hash[result], idn]
            num_hash[num] = idn


s = Solution()

# Test cases for Two Sum
print(s.twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1]
print(s.twoSum([3, 2, 4], 6))       # Expected: [1, 2]
print(s.twoSum([3, 3], 6))          # Expected: [0, 1]
