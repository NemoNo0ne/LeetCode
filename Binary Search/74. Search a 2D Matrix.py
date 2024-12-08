class Solution(object):
    def searchMatrix(self, matrix, target):
        row_top = 0
        row_bot = len(matrix) - 1

        while row_top <= row_bot:
            row_mid = (row_top + row_bot) // 2
            row = matrix[row_mid]

            if row[0] > target:
                row_bot = row_mid - 1
            elif row[-1] < target:
                row_top = row_mid + 1
            else:
                break
        else:
            return False

        left = 0
        right = len(row) - 1

        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


sol_74 = Solution()

# Test cases for 74. Search a 2D Matrix
print(sol_74.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3))  # Expected: True
print(sol_74.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 13)) # Expected: False
print(sol_74.searchMatrix([[1, 3, 5]], 3))                                         # Expected: True
print(sol_74.searchMatrix([[1, 3, 5]], 6))                                         # Expected: False
print(sol_74.searchMatrix([], 0))                                                  # Expected: False