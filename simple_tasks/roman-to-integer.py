class Solution(object):
    def isValid(self, s):
        return s.startswith("(") and s.endswith(")") or s.startswith("{") and s.endswith("}") or s.startswith("[") and s.endswith("]")

s = "()[]{}"
solution = Solution()
print(solution.isValid(s))
            