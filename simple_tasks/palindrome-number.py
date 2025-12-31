class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Convert the integer to string to check for palindrome
        str_x = str(x)
        
        # Check if the string is equal to its reverse
        return str_x == str_x[::-1]


solution = Solution()
print(solution.isPalindrome(121))  # True