class Linkedlist:
    def __init__(self, data):
        self.data=data
        self.next=None

# adding Nodes or Creating nodes

node1=Linkedlist(10)
node2=Linkedlist(20)
node3=Linkedlist(30)
node4=Linkedlist(60)

node1.next=node2
node2.next=node3
node3.next=node4

# Insert Element in Begining 

node1st=Linkedlist(340)
Head=node1st
varNormal=node1st
node1st.next=node1

# Inserting Element at 3rd POsition Or middle
NodeInsAt3rd=Linkedlist(290)
NodeInsAt3rd.next=node2
node1.next=NodeInsAt3rd

# Inserting Element At last position

lastNodeIns=Linkedlist(880)
while Head.next.next is not None:
    Head=Head.next
Head.next.next=lastNodeIns




while varNormal is not None:
    print(varNormal.data)
    varNormal=varNormal.next