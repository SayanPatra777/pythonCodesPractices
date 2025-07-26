# Node of Bonary tree
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        
if __name__=="__main__":
    rootOfTree1=TreeNode(2)
    rootOfTree1.leftChild=TreeNode(7)
    rootOfTree1.rightChild=TreeNode(10)

    rootOfTree1.leftChild.leftChild=TreeNode(15)
    rootOfTree1.rightChild.rightChild=TreeNode(27)
