class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1

        while left < right:
            result = numbers[left] + numbers[right]
            if result == target:
                return [left + 1, right + 1]
            elif result < target:
                left += 1
            else:
                right -= 1

sol_167 = Solution()

# Test cases for 167. Two Sum II - Input Array Is Sorted
print(sol_167.twoSum([2, 7, 11, 15], 9))  # Expected: [1, 2]
print(sol_167.twoSum([2, 3, 4], 6))       # Expected: [1, 3]
print(sol_167.twoSum([-1, 0], -1))        # Expected: [1, 2]
print(sol_167.twoSum([1, 2, 3, 4], 7))    # Expected: [3, 4]
