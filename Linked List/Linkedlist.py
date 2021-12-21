#Singly Linked List



class LL:
    def __init__(self,data):
        self.data=data
        self.next=None
def take_input():
    input_list=list(map(int,input().split()))
    head=None
    tail=None
    for ele in input_list:
        if ele==-1:
            break
        new_node=LL(ele)
        if head is None:
            head=new_node
            tail=new_node
        else:
            tail.next=new_node
            tail=tail.next
    return head

def insert_at_begin(head,x):
    new_node=LL(x)
    new_node.next=head
    head=new_node
    return head
def insert_at_end(head,x):
    new_node=LL(x)
    p=head
    while p.next is not None:
        p=p.next

    p.next=new_node
    return head

def insert_in_between(head,ele,x):
    new_node=LL(x)
    p=head
    while p is not None:
        if p.data==ele:
            break
        p=p.next
    
    new_node.next=p.next
    p.next=new_node
    return head
    
def delete_at_first(head):
    head=head.next
    return  head
def delete_last(head):
    p=head
    while p.next.next is not None:
        p=p.next
    p.next=None
    return head

def delete_in_between(head,x):
    p=head
    while p.next is not None:
        if p.next.data==x:
            break
        p=p.next
    p.next=p.next.next
    return head
    

def print_ll(head):
    p=head
    while p is not None:
        print(p.data,end="->")
        p=p.next 
    print("None")   

head=take_input()
    
     


# Doubly linked list

class Node:
    def __init__(self, value):
        self.info = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def print_list(self):
        if self.head is None:
            print("list is empty")
            return

        else:
            p= self.head
            while p is not None:
                print(p.info," ",end='')
                p = p.next
            print()
    def insert_at_start(selfself,data):
        temp = Node(data)
        temp.next= self.start
        self.start.prev = temp
        self.start=temp

    def insert_in_empty(self,data):
        temp=Node(data)
        self.start = temp

    def insert_at_end(self,data):
        temp=Node(data)
        p=self.start
        while p.next is not None:
            p=p.next
        p.next=temp
        temp.prev=p

    def insert_after(self,data,x):
        p=self.start
        while p is not None:
            if p.info==x:
                break
            p=p.next

        temp = Node(data)
        temp.next=p.next
        temp.prev=p
        p.next.prev = temp
        p.next=temp

    def insert_before(self, data, x):
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.next

        temp = Node(data)
        temp.prev-p.prev
        temp.next=p
        p.prev.next=temp
        p.prev= temp

    def delete_first_node(self):
        self.start=self.start.next
        self.start.prev=None


# Circular Linked list
class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class CircularLinkedList:
        def __init__(self):
            self.last = None

        def print_list(self):
            p=self.last.link
            while True:
                print(p.info," ",end="")
                p=p.link
                if p == self.last.link:
                    break
            print()

        def insert_in_begin(self,data):
            temp =Node(data)
            temp.link= self.last.link
            self.last.link=temp

        def insert_at_end(self,data):
            temp = Node(data)
            temp.link=self.last.link
            self.last.link=temp
            self.last=temp

        def delete_first_node(self):
            self.last.link=self.last.link.link

        def delete_last_node(self):
            p.link=self.last.link
            self.last=p

        def delete_in_between(self):
            p.link=p.link.link
