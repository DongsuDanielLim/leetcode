class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def sumVal(li):
    num = 0
    figure = 1
    while li != None:
        num = li.val * figure + num
        figure *= 10
        li = li.next
    return num
            
def addTwoNumbers(l1, l2):
    l1sum = sumVal(l1)
    l2sum = sumVal(l2)
    sumNum = l1sum + l2sum
    
    listSum = list(map(int, str(sumNum)))
    
    head = ListNode(listSum.pop())
    currentNode = head
    while len(listSum) > 0:
        cn = listSum.pop()
        currentNode.next = ListNode(cn)
        currentNode = currentNode.next
    
    return head

# (2 -> 4 -> 3) + (5 -> 6 -> 4)
# 7 -> 0 -> 8
list1Thir = ListNode(3)
list1Sec = ListNode(4)
list1Head = ListNode(2)
list1Sec.next = list1Thir
list1Head.next = list1Sec

list2Thir = ListNode(4)
list2Sec = ListNode(6)
list2Head = ListNode(5)
list2Sec.next = list2Thir
list2Head.next = list2Sec

addTwoNumbers(list1Head, list2Head)