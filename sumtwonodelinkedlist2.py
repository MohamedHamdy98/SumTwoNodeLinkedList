class LinkedNodeList:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedNodeList2:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

node1 = LinkedNodeList(1)
node2 = LinkedNodeList(2)

node3 = LinkedNodeList2(3)
node4 = LinkedNodeList2(4)

node1.next = node2
node3.next = node4

head = node1
head2 = node3

def addNode(head, v):
    node = LinkedNodeList(v)
    if head == None:
        head = node
    else:
        pointer = head
        while pointer.next != None:
            pointer = pointer.next
        pointer.next = node    

def sumNode(head, head2):
    pointer = head
    pointer2 = head2
    sum = 0
    while pointer != None and pointer2 != None:
        sum = pointer.value + pointer2.value
        pointer = pointer.next 
        pointer2 = pointer2.next 
        print(sum,'->', end=' ')

p = head
p2 = head2
while p != None and p2 != None:
    print(p.value,'->',p2.value)
    p = p.next
    p2 = p2.next

# addNode(head, 1)
sumNode(head, head2) 
