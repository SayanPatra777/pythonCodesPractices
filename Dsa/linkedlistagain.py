#singlylinked list
class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

def printLinkeedList(node1):
    #Printing the linked list
    head= node1
    while head is not None:
        print(head,end=' -> ')
        head = head.next
    print("None")





if __name__=='__main__':
    node1 = SinglyNode(10)
    node2 = SinglyNode(20)
    node3 = SinglyNode(30)
    node4 = SinglyNode(60)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    
# add data at 3rd position
    node_at_3rd = SinglyNode(40)
    node2.next = node_at_3rd
    node_at_3rd.next = node3
    
#swap 3rd & 4th node
    node2.next=node3
    node_at_3rd.next=node4
    node3.next=node_at_3rd
    
    print("1st linked list:")
    printLinkeedList(node1)
    
# create a new linked list & insert values with a loop
    head = SinglyNode(100)
    current = head
    for i in range(200, 1000, 100):
        new_node = SinglyNode(i)
        current.next = new_node
        current = new_node
    
    print("2nd linked list:")
    printLinkeedList(head)
    print(f"head = {head}")
    