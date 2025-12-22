class Solution(object):
    def getSneakyNumbers(self, nums):
        self.num = []
        for item in nums: 
            if item not in self.num:
                self.num.append(item)                   
        return self.num
    


nums = [0, 0, 1, 1]
solution = Solution()
print(solution.getSneakyNumbers(nums))
