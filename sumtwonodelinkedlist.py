class LinkedNodeList:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
node1 = LinkedNodeList(2)
node2 = LinkedNodeList(3)
node1.next = node2
head = node1
def addNode(head, v):
    node = LinkedNodeList(v)
    if head == None:
        head = node
    else:
        pointer = head
        while pointer.next != None:
            pointer = pointer.next
        pointer.next = node         
def sumNode(head):
    pointer = head
    sum = 0
    while pointer != None:
        sum += pointer.value
        pointer = pointer.next 
    print(sum)
addNode(head, 1)
sumNode(head) 
