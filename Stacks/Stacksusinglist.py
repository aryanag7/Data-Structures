
#Stack using array
class Stack:
    def __init__(self):
        self.__mystack=[]
        
#     to push an element into stack    

    def push(self,val):
        self.__mystack.append(val)
#      to pop an element from the stack   

    def pop(self):
        if self.isempty():
            return "stack underflow"
        self.__mystack.pop()
#      to return the element at top

    def top(self):
        return self.__mystack[-1]
    
    def isempty(self):
        if self.__mystack==[]:
            return True
        else:
            return False
#      to print the elements of stack

    def printele(self):
        for i in self.__mystack:
            print(i,end=" ")
        return 
s=Stack()
s.push(12)
s.push(21)
s.push(344)
s.push(4)
s.push(77)
s.push(646)
s.printele()

