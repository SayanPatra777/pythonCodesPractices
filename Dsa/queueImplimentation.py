# class Queue:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return len(self.items) == 0

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         return None

#     def size(self):
#         return len(self.items)
    
#     def peek(self):
#         if not self.is_empty():
#             return self.items[0]
#         return None
    
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
        queue=Queue()
        queue.push([root])
        

    
if __name__ == "__main__":   
    s=Queue()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())  # Output: 1
    print(s.peek())  # Output: 2
    print(s.size())  # Output: 2