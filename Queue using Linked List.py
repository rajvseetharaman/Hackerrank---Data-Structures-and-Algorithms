class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=None
    
class MyQueue():
    def __init__(self):
        self.head=None
        self.tail=None
    
    def peek(self):
        return self.head.data
        
    def pop(self):
        if(self.head!=None):
            self.head=self.head.next
        
    def put(self, value):
        if self.head==None:
            self.head=Node(value, None)
            self.tail=self.head
        else:
            p=Node(value, None)
            self.tail.next=p
            self.tail=p

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        
