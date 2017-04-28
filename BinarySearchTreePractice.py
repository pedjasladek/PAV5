import sys
import string
import random

def random_list (min,max,elements) :
    return random.sample(range(min,max),elements)

def string_generator(size = 3, chars = string.ascii_uppercase) :
    return ''.join(random.choice(chars) for _ in range(size))

def add_string(array, item, max_len):
    B.insert(0, item)
    return B[:max_len]

class Node :
    
    # Node constructor

    def __init__(self, x = None, y = None) :
        self.p = None
        self.r = None
        self.l = None
        self.data = Data(x,y)

class Data :

    # Data constructor: data contained in node

    def __init__(self, x = None , y = None) :
        self.value = x
        self.char = y

class Tree :

    # Tree constructor

    def __init__(self) :
        self.root = None

    def insert_node(self, x, y) :
        temp = Node(x,y)
        if (self.root == None) :
            self.root = temp
        else :
            self._insert_node(self.root, temp)

    def _insert_node(self, treeNode, newNode) :
        if (newNode.data.value <= treeNode.data.value) :
            if(treeNode.l == None) :
                treeNode.l = newNode
                newNode.p = treeNode
            else :
                self._insert_node(treeNode.l,newNode)
        else :
            if(treeNode.r == None) :
                treeNode.r = newNode
                newNode.p = treeNode
            else :
                self._insert_node(treeNode.r,newNode)         

    def in_order_tree_walk (self,node) :
        if(node != None) :
            self.in_order_tree_walk(node.l)
            print ("Printing data of node :", node.data.value, node.data.char)
            self.in_order_tree_walk(node.r)

    def tree_root_print (self) :
        if(self.root != None) :
            print ("Root of the tree is: ", self.root.data.value, self.root.data.char)

    def tree_minimum(self, node) :
        while(node.l != None):
            node = node.l
        return node

    def tree_maximum(self, node) :
        while(node.r != None) :
            node = node.r
        return node

    def tree_search(self, node, key):
        if(node == None or key == node.data.value):
            return node
        if(key < node.data.value):
            return self.tree_search(node.l, key)
        else :
            return self.tree_search(node.r, key)

    def iterative_tree_search(self, node, key) :
        while(node != None and key != node.data.value) :
            if(key < node.data.value) :
                node = node.l
            else :
                node = node.r
        return node
    
    def tree_succesor(self, node) :
        if(node != None or node != self.tree_maximum(node)) :
            if(node.r != None) :
                return self.tree_minimum(node.r)
            while(node.p != None and node == node.p.r) :
                node = node.p
            else:
                return node.p
        else:
            return None

    def tree_ancestor(self, node) :
        if(node != None or node != self.tree_minimum(node)) :
            if(node.l != None) :
                return self.tree_maximum(node.l)
            while(node.p != None and node == node.p.l) :
                node = node.p
            return node.p
        else:
            return None
    
    def tree_transplant(self,u,v) :
        if(u.p == None) :
            self.root = v
        elif(u == u.p.l) :
            u.p.l = v
        else :
            u.p.r = v
        if(v != None) :
            v.p = u.p

    def tree_delete(self, node) :
        if(node.l == None):
            self.tree_transplant(node,node.r)
        elif(node.r == None) :
            self.tree_transplant(node,node.l)
        else :
            y = self.tree_minimum(node.r)
            if(y.p != node):
                self.tree_transplant(y,y.r)
                y.r = node.r
                y.r.p = y
            self.tree_transplant(node, y)
            y.l = node.l
            y.l.p = y
    
    def in_order_walk_add(self, node) :
        global x
        if(node != None):
            self.in_order_walk_add(node.l)
            x.append(node)
            self.in_order_walk_add(node.r)

x = list()

tree = Tree()

A = random_list(0,30,10)
print A
print

B = [None] * 10

for i in range(0, len(B)) :
    B = add_string(B, string_generator() , 10)

print B
print

for i in range(0,len(A)) :
    tree.insert_node(A[i],B[i])

tree.in_order_tree_walk(tree.root)
print

tree.tree_root_print()
print

min = tree.tree_minimum(tree.root)
print ("Minimum of tree is :", min.data.value, min.data.char)
print

max = tree.tree_maximum(tree.root)
print ("Maximum of tree is :", max.data.value, max.data.char)
print

key = A[5]
invalid_key = 200
key_iter = A[6]

src = tree.tree_search(tree.root, key)

if (src != None) :
   print("Found the key", src.data.value, "and we searched for ", key)
else :
    print("No key", key, "found") 
print

src = tree.tree_search(tree.root, invalid_key)

if (src != None) :
   print("Found the key", src.data.value, "and we searched for ", invalid_key)
else :
    print("No key", invalid_key, "found") 
print

src = tree.iterative_tree_search(tree.root, key_iter)

if (src != None) :
   print("Found the key", src.data.value, "and we searched for ", key_iter)
else :
    print("No key", key_iter, "found") 
print

src = tree.iterative_tree_search(tree.root, invalid_key)

if (src != None) :
   print("Found the key", src.data.value, "and we searched for ", invalid_key)
else :
    print("No key", invalid_key, "found") 
print

successor_temp = tree.tree_search(tree.root,A[3])

successor = tree.tree_succesor(successor_temp)

if(successor != None) :
    print("Successor of key :", successor_temp.data.value, "is", successor.data.value)
else :
    print("Node with key: " ,successor_temp.data.value, "is maximum in tree and has no successor")
print

ancestor_temp = tree.tree_search(tree.root,A[3])

ancestor = tree.tree_ancestor(ancestor_temp)

if(ancestor != None) :
    print("Ancestor of key :", ancestor_temp.data.value, "is", ancestor.data.value)
else :
    print("Node with key: " ,ancestor_temp.data.value, "is minimum in tree and has no ancestor")
print

tree.insert_node(100,"WYR")
tree.insert_node(-20,"SGH")

print("Tree after inserting nodes with key's 100 and -20")
print

tree.in_order_tree_walk(tree.root)
print

print("Testing deletion of node maximum")
print

tree.tree_delete(tree.tree_maximum(tree.root))

tree.in_order_tree_walk(tree.root)
print

print("Testing deletion of node minimum ")
print

tree.tree_delete(tree.tree_minimum(tree.root))

tree.in_order_tree_walk(tree.root)
print

print("Testing deletion of node with key ", A[7])
print

tree.tree_delete(tree.tree_search(tree.root,A[7]))

tree.in_order_tree_walk(tree.root)
print

print("Printing array filled with sorted tree")
print

tree.in_order_walk_add(tree.root)
j = 0


for i in x:
    print("Element", j , "of array x has data: ", i.data.value, i.data.char)
    j += 1
print