class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None

    def print(self):
        return (self.data, self.next)


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_element(self, data):

        node = Node(data, self.head)
        self.head = node

    def print(self):

        if self.head is None:
            print("List is empty")

        itr = self.head

        string = " "

        while itr:

            string += str(itr.data) + " -->"
            itr = itr.next

        print(string)

    def insert_At_End(self, data):

        if self.head is None:
            self.head = Node(data, None)

            return

        itr = self.head

        while itr.next:

            itr = itr.next

        itr.next = Node(data, None)

    def insert_array(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_At_End(data)

    def get_length(self):

        itr = self.head

        count = 0

        while itr:
            itr = itr.next
            count = count+1

        return count

    def remove_at(self, index):

        if index < 0 or index > self.get_length():
            raise Exception("Invalid Syntax")

        if index == 0:
            return self.head


M = LinkedList()


M.insert_array(["Shankar", "Ram", "Saravanan"])


print(M.get_length())
