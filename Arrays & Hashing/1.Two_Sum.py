class Solution(object):
    def twoSum(self, nums, target):
        num_hash = {}
        for idn, num in enumerate(nums):
            result = target - num
            if result in num_hash:
                return [num_hash[result], idn]
            num_hash[num] = idn


sol_1 = Solution()


# Test cases for 1. Two Sum
print(sol_1.twoSum([2, 7, 11, 15], 9))    # Expected: [0, 1]
print(sol_1.twoSum([3, 2, 4], 6))         # Expected: [1, 2]
print(sol_1.twoSum([3, 3], 6))            # Expected: [0, 1]
print(sol_1.twoSum([1, 2, 3], 4))         # Expected: [0, 2]
