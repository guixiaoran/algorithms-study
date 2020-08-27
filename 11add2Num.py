# node class
# then lingked list class

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return  self.data

class Linkedlist:
    def __init__(self):
        self.head = None

    def print(self): # this function prints contents of linked list
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    # add node at the front of list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    # add node after a given node:
    def addin(self,node,newdata):
    # 1, given node;
    # change directions
        if node is None:
            return 'Nah'
        new_node = Node(newdata)
        new_node.next = node.next
        node.next = new_node
    #add node at the end
    def append(self,new_data):
        new_node = Node(new_data)
        # if empty
        if self.head is None:
            self.head = new_node
            return
        last= self.head
        while (last.next):
            last = last.next
        last.next = new_node

if __name__ == "__main__":
    a = Linkedlist()
    a.append(2)
    a.append(4)
    a.append(3)
    #a.print()
    b = Linkedlist()
    b.push(4)
    b.push(6)
    b.push(5)
    #b.print()

    c=Linkedlist()
    ini = Node(0)
    c.head = ini
    while a.head is not None and b.head is not None:
        temp1 = 0
        temp2 = 0
        temp = 0
        debt = 0
        if a.head is not None:
            temp1 = int(a.head.data)
            a.head = a.head.next
        if b.head is not None:
            temp2 = int(b.head.data)
            b.head = b.head.next
        if temp1+temp2 >9:
            temp = (temp1+temp2)%10
            debt+=1
        else:
            temp = temp1+temp2
        d=Node(debt)
        c.head.data+=temp
        print(c.head.data)
        c.head.next = d
        c.head = c.head.next






