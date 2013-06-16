#!/usr/bin/python
DEBUG = True

class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        #print "Node with value %s created" % value


    def __str__(self):
        return str(self.value)


class Tree:
    def __init__(self):
        self.root = None

    def add(self,value,**kwargs):

        if not self.root:
             self.root = Node(value)
             return self.root

        root = kwargs.get('root',self.root)


        if root is None:
             return Node(value)

        if (value > root.value):
            root.right = self.add(value,root=root.right)
        else:
            root.left = self.add(value,root=root.left)
        
        return root

    def exists(self, value, **kwargs):
        root = kwargs.get('root',self.root)
        if not root:
            return False
        
        if root.value == value:
            return True

        if value > root.value:
            return self.exists(value,root=root.right)
        else:
            return self.exists(value,root=root.left)

    def sum(self,**kwargs):

        root = kwargs.get('root',self.root)
        if not root:
            return 0

        return (self.sum(root=root.left) + root.value + self.sum(root=root.right))


    def inorder(self,**kwargs):
        root = kwargs.get('root',self.root)
        
        if not root:
            return
        if not root.left and not root.right:
            print root.value
            return
       
        self.inorder(root=root.left)
        print root.value
        self.inorder(root=root.right)

        
        

if __name__ == "__main__":
    x = Tree()
    x.add(4)
    x.add(5)
    x.add(2)
    x.add(7)
    x.add(1)


    print "Transverse tree in order"
    x.inorder()

    print "\nsum of tree is %d: \n"% x.sum()

    for i in range(0,11):
        print i,": ", x.exists(i)
