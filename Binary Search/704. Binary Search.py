class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


sol_704 = Solution()

# Test cases for 704. Binary Search
print(sol_704.search([-1, 0, 3, 5, 9, 12], 9))  # Expected: 4
print(sol_704.search([-1, 0, 3, 5, 9, 12], 2))  # Expected: -1
print(sol_704.search([5], 5))                   # Expected: 0
print(sol_704.search([5], -5))                  # Expected: -1
print(sol_704.search([], 3))                    # Expected: -1