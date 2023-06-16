# Last in first out


# PUSH POP

from collections import deque


stack = deque()


print(dir(stack))


class stack:

    def __init__(self):

        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        if len(self.container) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.container)

    def reverse_String(self, string):
        h = ''
        for i in string:
            self.push(i)
        for i in string:
            h += str(self.container.pop())
        return h


s = stack()
s.push(5)
s.push(10)
s.push(18)
print(s.peek())
print(s.is_empty())
print(s.container)


print(s.reverse_String("We will conquer covi-19"))
