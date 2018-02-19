class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def is_matched(expression):
    vals=expression
    s=Stack()
    for val in vals:
        if val in ['(','{','[']:
            s.push(val)
        elif val in [')','}',']']:
            if s.isEmpty():
                return False
            val2=s.pop()
            x=(val2,val)
            if x not in [('(',')'),('[',']'),('{','}')]:
                return False
        else:
            return False
    if s.isEmpty():
        return True
    else:
        return False
                

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
