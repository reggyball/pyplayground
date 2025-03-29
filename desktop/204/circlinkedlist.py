class Node:                                                                         #create the property of the node itself
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.next = None                                                            #initially you are creating a node in an empty list

class CircularLinkedList:                                                           #this class will manage all the nodes cause ito ang mismong list
    def __init__(self):                                                             
        self.head = None                                                            #initially you are making an empty list

    def get_prop(self, node, prop):                                                 #created to enable a dynamic search since multiple properties yung nasa node
        if prop == 'name':
            return node.name
        elif prop == 'age':
            return node.age
        elif prop == 'color':
            return node.color

    def search(self, target, prop = "name"):
        if self.head is None:                                                       #In comparison to linear, linear while loop already checks if list is empty because it uses truthy
            print (f"{target} is not found")
            return None

        current = self.head
        while True:                                                                 
            if self.get_prop(current, prop) == target:                                  #if the node contains the target you are looking for, return details
                print (f"""Found: {current.name}, 
Age: {current.age}, 
color: {current.color}""")
                return current
            elif current.next == self.head:                                              #stop if next is the head, meaning one full circle na natraverse
                break
            else: 
                current = current.next
        print(f"{target} is not found")      

    def delete(self, target):
        if self.head is None:                                      # if lists is empty
            print(f"{target} is not found, empty list")
            return False

        current = self.head                                        #assign a pointer to the head
        previous = None                                            #assign another pointer to track previous node

        if current.name == target:                                  #scenario 1 where the target is the head                           
            if current.next == self.head:                           #scenario 1.1 if the head is the target in a single node list
                self.head = None                                            
            else:
                while current.next != self.head:                    #scenario 1.2 delete head in a non singleton, this while loop searches for the last node 
                    current = current.next
                current.next = self.head.next                       #self.head.next is like a command asking to obtain the node next to self.head and assign it to current.next's container
                self.head = self.head.next
            print(f"{target} deleted")
            return True
        else: 
            while True:                                                  # scenario 2: target is somewhere in the middle of the list, 
                prev = current                                                 #so if its not the last in the list, traverse thru the nodes, using prev and current as pointers 
                current = current.next
                if current.name == target:
                    prev.next = current.next
                    print(f"{target} deleted")                              #orphan current #left side vars -> expects to obtain a new value, right side vars -> siya ung laman
                    return True
                elif current.next == self.head:                           #so if you are in the last node: declare target not found, return False     
                    print(f"{target} not found")
                    return False



    def insert(self, target, name, age, color):
        new_node = Node(name, age, color)

        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            print(f"{name} inserted")
        else:
            current = self.head
            while True:                                                                     #stop if next is the head, meaning one full circle na natraverse
                if current.name == target:
                   new_node.next = current.next
                   current.next = new_node
                   print(f"{name} inserted")
                   return
                elif current.next == self.head:
                    break 
                else: 
                    current = current.next
            return print(f"{target} not found")
                
            #last node is current (so susunod sa kanya gawin mong si new_node)
            

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        print(f"Name: {current.name}, Age: {current.age}, Color: {current.color}", end = " -> ")
        current = current.next

        while current != self.head:
            print(f"Name: {current.name}, Age: {current.age}, Color: {current.color}", end = " -> ")
            current = current.next
        print("....")




catprofile = CircularLinkedList()
# catprofile.search('Sunny')


catprofile.insert('', 'Appa', 5, 'white/black')
catprofile.insert('Appa', 'Sunny', 4, 'orange')
catprofile.insert('Appa', 'cat', 4, 'orange')


# catprofile.display()
catprofile.delete("cat")
catprofile.delete("cat")
# catprofile.delete('Sunny')
# catprofile.display()
# print(catprofile.search("new"))
print("Sunny not found")

