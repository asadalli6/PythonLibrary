import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        if (index == 0):
            self.insertAtBegin(data)
            
        position = 0
        current_node = self.head
        while (current_node != None and position+1 != index):
            position = position+1
            current_node = current_node.next

        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")


    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    def remove_first_node(self):
        if(self.head == None):
            return

        self.head = self.head.next

    def remove_last_node(self):

        if self.head is None:
            return

        current_node = self.head
        while(current_node != None and current_node.next.next != None):
            current_node = current_node.next

        current_node.next = None

    def remove_at_index(self, index):
        if self.head == None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    def remove_node(self, data):
        current_node = self.head

        if current_node.data == data:
            self.remove_first_node()
            return

        while(current_node != None and current_node.next.data != data):
            current_node = current_node.next

        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next

    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0

    def printLL(self):
        current_node = self.head
        counter = 0
        while(current_node):
            print(str(counter) + ': ' + current_node.data)
            current_node = current_node.next
            counter = counter + 1


def reverse(st):
    reversed = st.split(" ")[::-1]
    arr = []
    
    for i in st:
        arr.append(reversed)
        
    return ', '.join(arr)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#Python Main Loop
llist = LinkedList()
while True:
    print("===== Asad Alli To-Do List =====")
    print("1. Add Tasks")
    print("2. Show Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        taskName = input("What would you like to do: ")
        llist.insertAtEnd(taskName)
        print("Task added!")
        pau = input("Press any key to continue")

    if choice == '2':
        llist.printLL()
        print("Total tasks to complete: " + str(llist.sizeOfLL()))
        pau = input("Press any key to continue")

    if choice == '3':
        llist.printLL()
        tasktoremove = input("Which task have you completed: ")
        llist.remove_at_index(int(tasktoremove))
        if (tasktoremove > llist.sizeOfLL()):
            print("Subscript is out of range! Please try again.")
        else:
            print("Task has been completed!")
        pau = input("Press any key to continue")

    if choice == '4':
        print("Exiting Program...")
        exit()

    clear_terminal()
    pau = " "
