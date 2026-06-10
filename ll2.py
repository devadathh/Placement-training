class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=Node(data)
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
    def even(self):
        temp=self.head
        sum=0
        while temp:
            if temp.data%2==0:
                sum+=temp.data
            temp=temp.next
        return sum
l1=LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)
l1.display()
print(l1.even())