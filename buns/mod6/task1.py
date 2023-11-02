class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self, val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node

    def get(self, index):
        if index <0:
            raise IndexError
        current=self.head
        for i in range(index):
            if current is None:
                raise IndexError
            current=current.next
        if (current.next is None):
            raise IndexError
        return current.data

    def remove(self, index):
        if index <0:
            raise IndexError
        if index==0:
            if self.head is None:
                raise IndexError
            self.head=self.head.next
        else:
            current=self.head
            previous=None
            for i in range (index):
                if current is None:
                    raise IndexError
                previous=current
                current=current.next
            if current is None:
                raise IndexError
            previous.next=current.next

    def insert(self, n, val):
        if n<0:
            raise IndexError
        new_node=Node(val)
        if n==0:
            new_node.next=self.head
            self.head=new_node
        else:
            current=self.head
            for i in range (n-1):
                if current is None:
                    raise IndexError
                current=current.next
                if current is None:
                    raise IndexError
                current=current.next
            if current is None:
                raise IndexError
            new_node.next=current.next
            current.next = new_node

    def __iter__(self):
        current=self.head
        while current:
            yield  current.data
            current=current.next


list=LinkedList()

list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(5)
#for i in list:
    #print(i, end=' ')
#print(list.get(2))
#list.remove(1)
#for i in list:
    #print(i, end=' ')
list.insert(1, 2.5)
for i in list:
    print(i, end=' ')


