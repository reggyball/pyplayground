#single node
class Node:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.next = None    # no connections yet

#managing linkedlist as a whole
class LinkedList:
    def __init__(self):
        self.head = None        #the first node. Linked list starts empty

    def search(self, name):
        current = self.head
        while current:              #truty/falsy so while may laman si current, referencing to the nodes of list
            if current.name == name:
                return f"Result: Name: {current.name}, Age: {current.age}, Color: {current.color}"
            else:
                current = current.next
        return f"{name} is not found in the list"

    def insert_front(self, name, age, color):
        new_node = Node(name, age, color)           #create a new node with following info, next is none yet
        new_node.next = self.head                   #if already has nodes previously, point to it (the current head/previous first node)
        self.head = new_node                        #new_node becomes the first node(head of the list)

    def insert_end(self, name, age, color):
        new_node = Node(name, age, color)            #next is none by default as its not yet linked to anything
        if self.head == None:                        #if list is empty, make the new node the head
            self.head = new_node
        else:                                          #if not empty, start at the head
            current = self.head

            while current.next is not None:         #move forward until the last node
                current = current.next

            current.next = new_node                #attach new node at end

    def insert_after(self, prev_name, name, age, color):
        new_node = Node(name, age, color)          #creates  node that is not yet attached to anything
        current = self.head                        #initialize current to the first node

        while current is not None and current.name != prev_name:      #search for prev_name
            current = current.next                                    #move current to next node if current is not end or doesnt match prev_name
        
        #did not found prev_name
        if current is None:
            print(f"{prev_name} not found!")
            return

        #found prev_name                                    #attach new node in between prev_name and katabi ni prev
        #current = prev_name 
        new_node.next = current.next
        current.next = new_node
        
    def delete(self, name):
        current = self.head
        previous = None                                     #must have a reference to previous node para makabalik ka  sa connection na yon

        if current is None:                                 #scenario 1: list is empty                 
            print("list is empty")
            return

        if current.name == name:                            #scenario 2: if target is head
            self.head = current.next
            print(f"{name} deleted from list")
            return

        while current is not None and current.name != name: #scenario: target is somewhere in d middle
            previous = current
            current = current.next

        if current is None:
            print(f"{name} not found in the list")

        #remove current
        previous.next = current.next                            # change previous.next so that it no longer points to current. Instead, it skips current and points to current.next
        print(f"{name} deleted from the list")


    def display(self):
        current = self.head                          #start at the first node
        
        while current:                              
            print(f"Name: {current.name}, Age: {current.age}, Color: {current.color}")
            current = current.next                  #move to the next node until none
        print("End of list")


cats = LinkedList()
cats.insert_front("Sunny", "5", "orange")
cats.insert_front("Theo", "5", "Calico")
cats.insert_after("Theo", "Appa", "5", "White weird boy")


cats.display()
find = cats.search('Appa')
print(find)






































































