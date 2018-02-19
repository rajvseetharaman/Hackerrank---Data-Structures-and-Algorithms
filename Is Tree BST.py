""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
a=[]
def checkBST(root):
    inordertraversal(root)
    #print(a)
    if len([x for x in a if a.count(x) > 1])>0:
        return False
    if sorted(a)==a:
        return True
    else:
        return False

def inordertraversal(r):
    pointer=r
    if(pointer.left!=None):
        inordertraversal(pointer.left)
    a.append(pointer.data)
    if(pointer.right!=None):
        inordertraversal(pointer.right)

        
