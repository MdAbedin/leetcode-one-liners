class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return [[node1.__setattr__("next",node2),node1][1] for node1,node2 in pairwise([ListNode(int(digit)) for digit in "0"+str(int("".join([str(node.val) for node in list(takewhile(lambda x: x, accumulate(repeat(l1), lambda x,_: x.next)))[::-1]]))+int("".join([str(node.val) for node in list(takewhile(lambda x: x, accumulate(repeat(l2), lambda x,_: x.next)))[::-1]])))[::-1]])][0].next
