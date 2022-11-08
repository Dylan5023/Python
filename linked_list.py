# make Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


# use default value
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


# connecting Node to Node
node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

# add function
def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

# how to print
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)

node3 = Node(1.5)
search = True
while search:
    if node.data ==1:
        search = False
    else:
        node = node.next
node_next = node.next
node.next = node3
node3.next = node_next 

# another way to implement lindked_list
class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next



class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)

    def add(self, data):
        if self.head =='':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == '':
            print('there is no Node')
            return
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next
            

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

for data in range(0,10):
    linkedlist1.add(data)
linkedlist1.desc()


