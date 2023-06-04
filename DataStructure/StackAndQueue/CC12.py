
class Node :
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self,top=None):
        self.top = top

    def push(self,value):
        node = Node(value)
        #check if the statck is empty or not 
        # if its empty :
        if not self.top:
            self.top=node
        #IF NOT :
        else:
            node.next = self.top
            self.top = node

    def pop(self):
       
        #check if the statck is empty :
        if not self.top:
            raise Exception("There is nothing to remove in the stack")
        temp= self.top
        self.top = temp.next
        temp.next = None
        return temp.value

    def peek(self):
       
        if not self.top:
            raise Exception("This stake is empty so there is no top on it")
        else:
            return self.top.value
        
    def is_empty(self):
      
        if not self.top:
            return True
        return False  
    
    def __str__(self):
        current=self.top
        string=""
        while current:
            string+=f"{current.value.name}"
            string+=" -> "
            current=current.next
        return string+"None"    


class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

class AnimalShelter:
    def __init__(self,first=None):
        self.first=first
        self.second=Stack()
    
    def enqueue(self,animal):
       
        self.first.push(animal)

    def dequeue(self,pref):
       
        if pref not in ["cat","dog"]:
            return "Null"
        current=self.first.top
        if not current:
            raise Exception("The queue is empty nothing to remove")
        while current:
            self.second.push(current.value)
            self.first.pop()
            current=self.first.top
        temp=""
        current=self.second.top
        counter=0
        while current:
            if current.value.species==pref and counter==0 :
                temp=self.second.pop()
                counter+=1
            else:
                self.first.push(current.value)
                self.second.pop()
            current=self.second.top
        if temp=="":
            return "Null"
        return temp.species

#main
animal1=Animal("buddy","dog")
animal2=Animal("wishkers","cat")
animal3=Animal("wax","dog")

stack1=Stack()
queue1=AnimalShelter(stack1)
queue1.enqueue(animal1)
queue1.enqueue(animal2)
queue1.enqueue(animal3)

print(stack1)
print(queue1.dequeue("cat"))
print(stack1)