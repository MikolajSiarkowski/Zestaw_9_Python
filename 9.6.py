class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)
    

def count_leafs(top):
    if top == None:
        return 0
    if top.left == None and top.right == None:
        return 1
    else:
        return count_leafs(top.left)+count_leafs(top.right)
        
def count_total(top):
    if top == None:
        return 0;
    if top.left == None and top.right == None:
        return top.data
    else:
        return top.data+count_total(top.left)+count_total(top.right)

