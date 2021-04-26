#Singly Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("List is empty.")
        else:
            p = self.head
            while p is not None:
                print(p.value, end='->')
                p = p.next

    def count_nodes(self):
        c = 0
        p = self.head
        while p is not None:
            c = c + 1
            p = p.next
        print("Count of nodes: " + str(c))

    def search_element(self, element):
        pos = 1
        p = self.head
        while p is not None:
            if p.value == element:
                print("Element found at position: " + str(pos))
                return pos

            p = p.next
            pos = pos + 1

        print("Element not found in the linked list.")

    def insert_at_start(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insert_at_end(self, value):
        temp = Node(value)
        p = self.head
        while p.next is not None:
            p = p.next

        p.next = temp
        temp.next = None


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
