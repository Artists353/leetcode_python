# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        self.array = []
        for i, u in enumerate(head):
            self.array.append(u)
        
        self.array = list(set(self.array))
        return self.array
        

head = [1,1,2]    
solution = Solution()
print(solution.deleteDuplicates(head))