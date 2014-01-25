#!/usr/bin/python


class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)
        

class myList:
    def __init__(self, n = None):
        self.head = n
        print "created a list";
    
    def add(self,value):
        if not self.head:
            self.head = Node(value)
        else:
            temp = self.head;
            while (temp.next):
                temp = temp.next
            temp.next = Node(value)


    def __str__(self):
         temp  = self.head; 
         myvals = ""
         while (temp.next):
             myvals += str(temp) + ", "
             temp = temp.next
         
         myvals += str(temp);

         return myvals;
         


l = myList()

l.add(5)
l.add(7)
l.add(2)
l.add(4)
l.add(8)
l.add(19)

for i in xrange(20):
    l.add(i)


print l
