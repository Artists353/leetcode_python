# Вам даны заголовки двух отсортированных связанных списков list1и list2.

# Объедините два списка в один отсортированный . Список должен быть получен путём объединения узлов первых двух списков.

# Возвращает заголовок объединенного связанного списка .

# Definition for singly-linked list.     
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return [x for i in zip(list1, list2) for x in i]
    

list1 = [1,2,3]
list2 = [1,2,3,4]
solution = Solution()
print(solution.mergeTwoLists(list1, list2))



        