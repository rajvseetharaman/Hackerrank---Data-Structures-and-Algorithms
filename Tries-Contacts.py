class Node:
    def __init__(self,children,endofword,countofword):
        self.children=children
        self.endofword=endofword
        self.countofword=countofword

def contact_add(contact,root):
    pointer=root
    for i,letter in enumerate(contact):
        if letter not in pointer.children.keys():
            if i<len(contact)-1:
                pointer.children[letter]=Node({},False,0)
            else:
                pointer.children[letter]=Node({},True,0)
            pointer = pointer.children[letter]
        else:
            pointer=pointer.children[letter]
        pointer.countofword+=1

def contact_find(contact,root):
    pointer=root
    counter=0
    for i,letter in enumerate(contact):
        if letter in pointer.children.keys():
            pointer=pointer.children[letter]
        else:
            return 0
    return(pointer.countofword)
            
        
n = int(input().strip())
root=Node({},False,0)
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        contact_add(contact,root)
    if op == 'find':
        print(contact_find(contact,root))
