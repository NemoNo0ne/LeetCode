class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if nums[i] > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:

                three_sum = a + nums[left] + nums[right]

                if three_sum == 0:
                    result.append([a, nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                elif three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1

        return result

# Create an instance of the Solution class
sol_15 = Solution()

# Test cases for the problem 15. 3Sum
print(sol_15.threeSum([-4, -2, -2, 0, 0, 2, 2, 4]))  # Expected: [[-4, -2, 2], [-4, -2, 2], [-2, -2, 2], [-2, 0, 2]]
print(sol_15.threeSum([-2, 0, 1, 1, 2, 2]))          # Expected: [[-2, 0, 2], [-2, 1, 1]]
print(sol_15.threeSum([0, 0, 0]))                  # Expected: [[0, 0, 0]]
print(sol_15.threeSum([-1, 0, 1, 2, -1, -4]))      # Expected: [[-1, -1, 2], [-1, 0, 1]]
print(sol_15.threeSum([1, 2, -2]))                 # Expected: []