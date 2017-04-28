import sys
import random
import string

global x

############################################################################################

"""
         Functions for getting random integer, string and for adding string in list
"""

############################################################################################


# Random integer list generator.

def random_list (min,max,elements):
    return random.sample(range(min,max),elements)

# Random string generator.

def string_generator(size = 5, chars = string.ascii_uppercase) :
    return ''.join(random.choice(chars) for _ in range(size))

# Inserting string to list and resizing.

def add(B, item, max_len):
    B.insert(0, item)
    return B[:max_len]

############################################################################################

"""
                                        Classes for tree
"""

############################################################################################


# Class for nodes

class Node :
    
    # Node constructor

    def __init__(self,x = None,y = None) :
        self.p = None
        self.l = None
        self.r = None
        self.data = Data(x, y)

# Class for nodes data

class Data :

    # Data constructor

    def __init__(self, x = None, y = None) :
        self.value = x
        self.char = y

# Class tree

class Tree:

    # Tree constructor

    def __init__(self) :
        self.root = None

    # Methode for inserting nodes to tree

    def tree_insert(self,x,y) :
        temp = Node(x,y)
        if (self.root == None) :
            self.root = temp
        else :
            self._tree_insert(self.root, temp)

    # Methode for recursive adding
    
    def _tree_insert(self, treeNode, newNode) :
        if(newNode.data.value <= treeNode.data.value) :
            if(treeNode.l == None):
                newNode.p = treeNode
                treeNode.l = newNode
            else :
                self._tree_insert(treeNode.l, newNode)
        else :
            if(treeNode.r == None) :
                newNode.p = treeNode
                treeNode.r = newNode
            else :
                self._tree_insert(treeNode.r, newNode)

    # Methode for going through tree and printing nodes in order

    def tree_in_order_walk(self,node) :
        if(node != None) :
            self.tree_in_order_walk(node.l)
            print("Printing node data : ", node.data.value, node.data.char)
            self.tree_in_order_walk(node.r)
    
    # Methode for printing root of a tree

    def tree_root_print(self) :
        if(self.root != None) :
            print("Printing root data", self.root.data.value, self.root.data.char)

    # Methode for searching key in tree (at begining current is root)

    def tree_search(self, node, key):
        if(node == None or key == node.data.value):
            return node
        if(key < node.data.value):
            return self.tree_search(node.l, key)
        else :
            return self.tree_search(node.r, key)

    # Methode for itterative searching key in tree (at begining current is root)

    def iterative_tree_search(self, node, key) :
        while(node != None and key != node.data.value) :
            if(key < node.data.value) :
                node = node.l
            else :
                node = node.r
        return node

    # Methode for finding tree minimum

    def tree_minimum(self, node) :
        while(node.l != None) :
            node = node.l
        return node

    # Methode for finding tree maximum

    def tree_maximum(self, node) :
        while(node.r != None) :
            node = node.r
        return node

    # Methode for finding node successor

    def tree_succesor(self, node) :
        if(node.r != None) :
            return self.tree_minimum(node.r)
        while(node.p != None and node == node.p.r) :
            node = node.p
        return node.p

    # Methode for finding node ancesstor

    def tree_ancestor(self, node) :
        if(node.l != None) :
            return self.tree_maximum(node.l)
        while(node.p != None and node == node.p.l) :
            node = node.p
        return node.p

    # Methode transplant

    def tree_transplant(self, u, v) :
        if(u.p == None) :
            self.root = v
        elif(u == u.p.l) :
            u.p.l = v
        else :
            u.p.r = v
        if(v != None) :
            v.p = u.p

     # Methode for deleting node from tree

    def tree_delete(self, node):
        if(node.l == None) :
            tree.tree_transplant(node, node.r)
        elif(node.r == None) :
            tree.tree_transplant(node, node.l)
        else :
            y = tree.tree_minimum(node.r)
            if(y.p != node) :
                tree.tree_transplant(y,y.r)
                y.r = node.r
                y.r.p = y
            tree.tree_transplant(node,y)
            y.l = node.l
            y.l.p = y

    # Methode for walking through the tree and adding nodes to the list

    def tree_in_order_walk_with_retval(self,node) :
        global x
        if(node != None) :
            self.tree_in_order_walk_with_retval(node.l)
            x.append(node)
            self.tree_in_order_walk_with_retval(node.r)

############################################################################################

"""
                                        TESTING
"""

############################################################################################


# Making tree

tree = Tree()

# Making list of random integers and printing it.

print("####################################################################################")
print
print("Making list of random integers and printing it.")
print

A = random_list(0,30,10)

print(A)

print
print("####################################################################################")
print

# Initializing list of 10 elements.

B = [None] * 10

# Adding random strings to list and printing it.

print("####################################################################################")
print
print("Adding random strings to list and printing it.")
print

for i in range(0,len(B)):
    B = add(B, string_generator(), 10)

print(B)

print
print("####################################################################################")
print

# Making object of class Data and printing it.

print("####################################################################################")
print
print("Making object of class Data and printing it.")
print

d = Data(A[0],B[0])

print(d.value,d.char)

print
print("####################################################################################")
print

# Adding list A,B to tree (testing add methode).

for i in range(0,len(A)) :
    tree.tree_insert(A[i],B[i])

# Testing in order walk.

print("####################################################################################")
print
print("Testing in order walk")
print


tree.tree_in_order_walk(tree.root)

print
print("####################################################################################")
print

# Testing root data print.

print("####################################################################################")
print
print("Testing root data print.")
print

tree.tree_root_print()

print
print("####################################################################################")
print

key = A[5]
key_i = A[6]
key_invalid = 100

# Testing tree search for valid key.

print("####################################################################################")
print
print("Testing tree search for valid key.")
print

f_k = tree.tree_search(tree.root, key)

if (f_k != None) : 
    print("Found the key", f_k.data.value, "and we searched for ", key)
else :
    print("No key", key, "found")

print
print("####################################################################################")
print

# Testing tree search for invalid key (non existing).

print("####################################################################################")
print
print("Testing tree search for invalid key (non existing).")
print

f_k = tree.tree_search(tree.root, key_invalid)

if (f_k != None) : 
    print("Found the key", f_k.data.value, "and we searched for ", key_invalid)
else :
    print("No key", key_invalid, "found")

print
print("####################################################################################")
print

# Testing iterative search for valid key.

print("####################################################################################")
print
print("Testing iterative search for valid key.")
print

f_k_i = tree.iterative_tree_search(tree.root, key_i)

if (f_k_i != None) : 
    print("Found the key", f_k_i.data.value, "and we searched for ", key_i)
else :
    print("No key", key_i, "found")

print
print("####################################################################################")
print

# Testing iterative tree search for invalid key (non existing).

print("####################################################################################")
print
print("Testing iterative tree search for invalid key (non existing).")
print

f_k_i = tree.iterative_tree_search(tree.root, key_invalid)

if (f_k_i != None) : 
    print("Found the key", f_k_i.data.value, "and we searched for ", key_invalid)
else :
    print("No key", key_invalid, "found")

print
print("####################################################################################")
print

# Testing for finding tree minimum.

print("####################################################################################")
print
print("Testing for finding tree minimum.")
print

min = tree.tree_minimum(tree.root)

print("Tree minimum data", min.data.value, min.data.char)

print  
print("####################################################################################")
print

# Testing for finding tree maximum.

print("####################################################################################")
print
print("Testing for finding tree maximum.")
print

max = tree.tree_maximum(tree.root)

print("Tree maximum data", max.data.value, max.data.char)

print  
print("####################################################################################")
print

# Testing for finding nodes successor (used iterative tree search to pick element 4 from tree).

print("####################################################################################")
print
print("Testing for finding nodes successor.")
print

current = tree.iterative_tree_search(tree.root,A[4])

successor = tree.tree_succesor(current)

print("Successor of node", current.data.value, current.data.char," is", successor.data.value, successor.data.char)

print  
print("####################################################################################")
print


# Testing for finding nodes ancestor (used iterative tree search to pick element 7 from tree).

print("####################################################################################")
print
print("Testing for finding nodes ancestor.")
print

current_a = tree.tree_search(tree.root,A[7])

ancestor = tree.tree_ancestor(current_a)

print("Ancestor of node", current_a.data.value, current_a.data.char," is", ancestor.data.value, ancestor.data.char)

print  
print("####################################################################################")
print


# Testing insertion of new elements.

print("####################################################################################")
print
print("Testing insertion of new elements.")
print
print("Inserting 110 in tree.")
print

tree.tree_insert(110,"GWAXH")

print("Printing tree in order after inseting 110 in tree.")
print

tree.tree_in_order_walk(tree.root)

print
print("Inserting -5 in tree.")
print

tree.tree_insert(-5,"OQJSN")

print("Printing tree in order after inseting -5 in tree.")
print

tree.tree_in_order_walk(tree.root)

print  
print("####################################################################################")
print

# Testing for finding tree minimum after inserting 110 and -5 in tree.

print("####################################################################################")
print
print("Testing for finding tree minimum.")
print

min = tree.tree_minimum(tree.root)

print("Tree minimum data", min.data.value, min.data.char)

print  
print("####################################################################################")
print

# Testing for finding tree maximum after inserting 110 and -5 in tree.

print("####################################################################################")
print
print("Testing for finding tree maximum.")
print

max = tree.tree_maximum(tree.root)

print("Tree maximum data", max.data.value, max.data.char)

print  
print("####################################################################################")
print

# Testing for deleting of node with minimum key.

print("####################################################################################")
print
print("Testing for deleting of node with minimum key.")
print

node_delete = tree.tree_minimum(tree.root)

print("Tree before deleting node with minimum key", node_delete.data.value)
print

tree.tree_in_order_walk(tree.root)
print

deleted = tree.tree_delete(node_delete)

print("Tree after deleting minimum.")
print

tree.tree_in_order_walk(tree.root)

print  
print("####################################################################################")
print

# Testing for deleting of node with maximum key.

print("####################################################################################")
print
print("Testing for deleting of node with maximum key.")
print

node_delete = tree.tree_maximum(tree.root)

print("Tree before deleting node with maximum key", node_delete.data.value)
print

tree.tree_in_order_walk(tree.root)
print

deleted = tree.tree_delete(node_delete)

print("Tree after deleting maximum.")
print

tree.tree_in_order_walk(tree.root)

print  
print("####################################################################################")
print

# Testing for deleting of random node.

print("####################################################################################")
print
print("Testing for deleting of node with random key.")
print

node_delete = tree.tree_search(tree.root,A[5])

print("Tree before deleting node with key", A[5])
print

tree.tree_in_order_walk(tree.root)
print

deleted = tree.tree_delete(node_delete)

print("Tree after deleting node with key", A[5])
print

tree.tree_in_order_walk(tree.root)

print  
print("####################################################################################")
print

# Testing in order walk through the tree with adding arrays to list.

print("####################################################################################")
print
print("Testing in order walk through the tree with adding arrays to list.")
print

x = list()
j = 0

tree.tree_in_order_walk_with_retval(tree.root)

for i in x:
    print("Element", j,"of array has tree data:",i.data.value, i.data.char)
    j += 1
    
print  
print("####################################################################################")
print


