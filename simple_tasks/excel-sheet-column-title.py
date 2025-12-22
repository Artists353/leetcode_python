class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        

        result = []
        while columnNumber > 0:
            columnNumber -= 1  # Adjust for 0-indexing
            remainder = columnNumber % 26
            result.append(chr(remainder + ord('A')))
            columnNumber //= 26
        return ''.join(reversed(result))
    
solution = Solution()# Example usage:
print(solution.convertToTitle(1))    # Output: "A"