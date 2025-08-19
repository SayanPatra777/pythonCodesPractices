class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def size(self):
        return len(self.items)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=Queue()
        ans=[]
        queue.push(root)
        ans.append([root.val])
        while queue.size():
            level=[]
            for _ in range (queue.size()):
                front=queue.pop()
                if front.left:
                    level.append(front.left.val)
                    queue.push(front.left)
                if front.right:
                    level.append(front.right.val)
                    queue.push(front.right)
                    # Edit the code from here & it will be level order traversal ZIGZAG 😁
            if level:
                ans.append(level) # & when you return the ans reverse it solve another question that state level traversal Bottom up 
        return ans
    
    # Basically BFS