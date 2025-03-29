class Node:                                                 #node related activities
    def __init__(self, value):
        self.value = value                                  #nts: node -object | node.value - data/value un
        self.leftChild = None
        self.rightChild = None

    def inorder(self):  
        ordered_node = []  
                                                             #works in a single node at a time so placed here, visits left child, current node, right child                                                
        if self.leftChild:                                   #recursively call inorder() to ask the current node to visit its LChild
            ordered_node += self.leftChild.inorder()         #adds all left child to list

        ordered_node.append(self.value)                      #adds value of the current node
        
        if self.rightChild:                                 #adds all right child to list
             ordered_node += self.rightChild.inorder()

        return ordered_node

    def preorder(self):
        ordered_node = []  
        ordered_node.append(self.value)  

        if self.leftChild:
            ordered_node += self.leftChild.preorder()
        
        if self.rightChild:
            ordered_node += self.rightChild.preorder()

        return ordered_node

    def postorder(self):
        ordered_node = []  
        
        if self.leftChild:
            ordered_node += self.leftChild.postorder()
        
        if self.rightChild:
            ordered_node += self.rightChild.postorder()

        ordered_node.append(self.value) 
        return ordered_node 


class Tree:                                                                     #tree related activties                                  
    def __init__(self):
        self.root = None

    # Helper Methods
    def is_empty(self):
        return self.root is None

    def display(self):
        if self.is_empty():
            return
        ordered_node = self.inorder()
        print(" ".join(map(str, ordered_node)))


    #traversals
    def inorder(self):                                                          #delegates traversal to individual nodes;hence node class
        if self.root:                                                           #nodes itself would have to be the one responsible for visiting its own L/R child
            return self.root.inorder()
        else:
            print("Tree empty")

    def preorder(self):
        if self.root:
            return self.root.preorder()

    def postorder(self):
        if self.root:
            return self.root.postorder()

    def insert(self, value):
        #create a new node
        new_node = Node(value)                                                  #instantiate a newnode

       # if tree is empty, new node becomes root
        if self.is_empty():
         self.root = new_node
         return True
        
        #check value if existing and return the position to insert                                                                #if tree contains nodes, compare, add to leaf
        node, parent = self.search(value)

        #if existing, then duplicate
        if node:
            return False
        
        #if not
        # and its less than parent, attach as a left child
        elif new_node.value < parent.value:
            parent.leftChild = new_node
        
        #or if greater than the parent, attach as a right child
        else:
            parent.rightChild = new_node
        return True

    def search(self, value):
        current_node = self.root
        parent = None 
        
        #if tree is empty
        if self.is_empty():
            print("Tree empty")
            return None, None

        #if value is at the tree
        while current_node and current_node.value != value:
           parent = current_node
           if  value < current_node.value:
                current_node = current_node.leftChild
           else:
                current_node = current_node.rightChild

        return current_node, parent

    def delete(self, value):
        current_node = self.root
        
        #if tree is empty                                       
        if self.is_empty():
            print("Tree Empty")
            return False
   
        #find the node if it exist
        target, parent = self.search(value)

        if target == None:
            print("Target not found")
            return False
        else:
            #if target node has no children
            if target.leftChild == None and target.rightChild == None:
                if parent == None:                                           #if root node is the target
                    self.root = None;
                elif parent.leftChild.value == target.value:
                    parent.leftChild = None
                else:
                    parent.rightChild = None
                return True

            #if target has one child
            elif (target.leftChild != None) ^ (target.rightChild != None):
                targetChild = target.leftChild if target.leftChild else target.rightChild
                if parent == None:
                    self.root = targetChild
                elif target == parent.leftChild: 
                    parent.leftChild = targetChild
                else:
                    parent.rightChild = targetChild
                return True

            #if target has two child
            elif target.leftChild and target.rightChild:
                
                #find the successor using inorder
                successor = None
                ordered_node = self.inorder()

                #find successor - value to the right of target in orderd list
                target_index = ordered_node.index(target.value)
                successor_index = target_index + 1
                successor = ordered_node[successor_index]
                
                #find node of target successor / #connect node ts to parent
                successor_node, parent_s = self.search(successor)
               
                #prepping the successor
                #assign left child
                successor_node.leftChild = target.leftChild

                #IF PARENT'S SUCCESSOR IS NOT A DIRECT CHILD
                if target != parent_s:
                    parent_s.leftChild = successor_node.rightChild
                    successor_node.rightChild = target.rightChild

                #root is the target
                if parent == None:
                    self.root = successor_node
                #2child
                elif target == parent.leftChild:
                    parent.leftChild = successor_node
                else:
                    parent.rightChild = successor_node
                   
        
        return True
      
    




##################### DEMO #######################

#https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/?fbclid=IwZXh0bgNhZW0CMTEAAR1dBja9vAFJyK7WMDhLvzvHvx1wBWxe_59ZfpXYD_ucjq5iEcReANvFz1Q_aem_wkofszSFVpcX-WEh9hitRw
def find_height(root):
    if not root:
        return -1

    left_height = find_height(root.leftChild)
    right_height = find_height(root.rightChild)

    return max(left_height, right_height) + 1
def preorder(root, row, col, height, ans):
    if not root:
        return

    # Place the current node's value in the matrix
    ans[row][col] = str(root.value)

    # Calculate offset for child positions
    offset = 2 ** (height - row - 1)

    # Traverse the left subtree
    if root.leftChild:
        preorder(root.leftChild, row + 1, col - offset, 
                 height, ans)

    # Traverse the right subtree
    if root.rightChild:
        preorder(root.rightChild, row + 1, col + offset, 
                 height, ans)
def tree_to_matrix(root):
  
    # Find the height of the tree
    height = find_height(root)

    # Rows are height + 1; columns are 2^(height+1) - 1
    rows = height + 1
    cols = 2 ** (height + 1) - 1

    # Initialize 2D matrix with empty strings
    ans = [["" for _ in range(cols)] for _ in range(rows)]

    # Populate the matrix using preorder traversal
    preorder(root, 0, (cols - 1) // 2, height, ans)

    return ans
def print_2d_array(arr):
    for row in arr:
        for cell in row:
            if cell == "":
                print(" ", end="")
            else:
                print(cell, end="")
        print()


def insertToTree():
    #create the BST
    tree = Tree()
    tree.insert(10)
    print("\n\ninsert 10")
    print_2d_array(tree_to_matrix(tree.root))
    print("\n\n\n-------------------------\ninsert 5\n\n")

    tree.insert(5)
    print_2d_array(tree_to_matrix(tree.root))
    print("\n\n\n-------------------------\ninsert 15\n\n")


    tree.insert(15)
    print_2d_array(tree_to_matrix(tree.root))
    print("\n\n\n-------------------------\ninsert 3\n\n")


    tree.insert(3)
    print_2d_array(tree_to_matrix(tree.root))
    print("\n\n\n-------------------------\ninsert 7\n\n")


    tree.insert(7)
    print_2d_array(tree_to_matrix(tree.root))

    print("\n\n\n-------------------------\noutput using inorder traversal\n\n")
    tree.display()
# insertToTree()

def searchEmptyTree():
    print('\n\n')
    tree = Tree()

    print('Searching: 24...\n')
    node, parent = tree.search(24)
    print('Returned: ', node, "\nparent: ", parent)
    print('\n\n-------------------------')
# searchEmptyTree()

def searchInTreeNotFound():
    print('\n')
    tree = Tree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    
    print_2d_array(tree_to_matrix(tree.root))
    print('\n')


    print('Searching: 24...\n')
    node, parent = tree.search(24)
    print('Returned:', node, '\nparent:', parent.value)
    print('Node not found')
    print('\n\n-------------------------\n\n')
# searchInTreeNotFound()

def searchInTreeFound():
    print('\n')
    tree = Tree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)

    tree.insert(3)
    tree.insert(7)
    
    print_2d_array(tree_to_matrix(tree.root))
    print('\n')

    print('Searching: 7...\n')
    node, parent = tree.search(7)
    print('Returned:', node.value, '\nparent:', parent.value)
    print('\n\n-------------------------\n\n')
# searchInTreeFound()

def deleteFromEmptyTree():
    print('\n')
    tree = Tree()
   
    print('Deleting: 10...')
    success = tree.delete(10)
    print('Success:', success, '\n')
# deleteFromEmptyTree()

def deleteNotFound():
    print('\n')
    tree = Tree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    
    print_2d_array(tree_to_matrix(tree.root))
    print('\n')


    print('Deleting: 24...')
    success = tree.delete(24)
    print('Success:', success)
    print('\n')
    print_2d_array(tree_to_matrix(tree.root))
    print('\n')
# deleteNotFound()

def delete2ChildrenRootSuccessorNotDirect():
    print('\n')
    tree = Tree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    tree.insert(11)
    tree.insert(12)
    
    print_2d_array(tree_to_matrix(tree.root))
    print('\n')


    print('Deleting: 10...')
    success = tree.delete(10)
    print('Success:', success)
    print('\n')
    print_2d_array(tree_to_matrix(tree.root))
    print('\n')
# delete2ChildrenRootSuccessorNotDirect()

def delete2ChildrenRootSuccessorDirectChild():
    print('\n')
    tree = Tree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    
    print_2d_array(tree_to_matrix(tree.root))
    print('\n')


    print('Deleting: 5...')
    success = tree.delete(5)
    print('Success:', success)
    print('\n')
    print_2d_array(tree_to_matrix(tree.root))
    print('\n')
# delete2ChildrenRootSuccessorDirectChild()

