class Node: 
    def __init__(self, key): 
        self.key =  key 
        self.left = None
        self.right = None
  
# Finds the path from root node to given root of the tree. 
# Stores the path in a list path[], returns true if path  
# exists otherwise false 
def findPath( root, path, k): 
  
    if root is None: 
        return False
  
    # Store this node is path vector. The node will be 
    # removed if not in path from root to k 
    path.append(root.key) 
  
    # See if the k is same as root's key 
    if root.key == k : 
        return True
  
    # Check if k is found in left or right sub-tree 
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))): 
        return True 
  
    # If not present in subtree rooted with root, remove 
    # root from path and return False 
       
    path.pop() 
    return False
  
# Returns LCA if node a , b are present in the given 
# binary tre otherwise return -1 
def lca(root, a, b): 
  
    path1 = [] 
    path2 = [] 
   
    if (not findPath(root, path1, a) or not findPath(root, path2, b)): 
        return -1 
  
    # Compare the paths to get the first different value 
    i = 0 
    while(i < len(path1) and i < len(path2)): 
        if path1[i] != path2[i]: 
            break
        i += 1
    return path1[i-1] 
  

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7)
root.right.right.right = Node(8) 
  
print "LCA(4, 5) = %d" %(lca(root, 4, 5,)) 
print "LCA(4, 6) = %d" %(lca(root, 4, 6)) 
print "LCA(3, 4) = %d" %(lca(root,3,4)) 
print "LCA(2, 4) = %d" %(lca(root,2, 4))
print "LCA(6, 8) = %d" %(lca(root,6, 8))
