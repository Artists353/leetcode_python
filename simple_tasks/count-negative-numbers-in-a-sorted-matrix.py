class Solution:
    def countNegatives(self, grid):
        count = 0
        # Iterate through each row and each number in the row
        for row in grid:
            # Count negative numbers in the current row
            for num in row:
                if num < 0:
                    count += 1
        return count
    

solution = Solution()
grid = [[4, 3, 2, -1],
        [3, 2, 1, -1],
        [1, 1, -1, -2],
        [-1, -1, -2, -3]]
print(solution.countNegatives(grid))  # Output: 8