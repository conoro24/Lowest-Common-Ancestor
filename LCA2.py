class Node: 
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
# Function to find LCA of a and b. The function assumes 
# that both a and b are present in BST 
def lca(root, a, b): 
      
    if root is None: 
        return None
  
    # If both a and b are smaller than root, then LCA lies in left 
    if(root.data > a and root.data > b): 
        return lca(root.left, a, b) 
  
    # If both a and b are greater than root, then LCA lies in right  
    if(root.data < a and root.data < b): 
        return lca(root.right, a, b) 
  
    return root 
  

root = Node(6) 
root.left = Node(4) 
root.right = Node(8) 
root.left.left = Node(3) 
root.left.right = Node(5) 
root.left.right.left = Node(1) 
root.left.right.right = Node(10) 
  
a = 5 ; b = 1
t = lca(root, a, b) 
print ("LCA of %d and %d is %d" %(a, b, t.data)) 
  
a = 3 ; b = 10
t = lca(root, a, b) 
print ("LCA of %d and %d is %d" %(a, b , t.data)) 
  
a = 5 ; b = 8
t = lca(root, a, b) 
print ("LCA of %d and %d is %d" %(a, b, t.data))
