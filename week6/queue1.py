class Stack:

    def __init__(self, capacity):

        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def isempty(self):
        return self.top == -1

    def isfull(self):
        return self.top == self.capacity - 1

    def push(self, item):

        if self.isfull():
            print('Stack already overflowed cannot push items')
            return False

        self.top += 1
        self.stack[self.top] = item
        print('Insertion succeeded')
        return True

    def pop(self):

        if self.isempty():
            print('The stack is underflowed')
            return None

        popped_item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1

        print('Popped item:', popped_item)
        return popped_item

    def peek(self):

        if self.isempty():
            print('Stack is underflowed')
            return None

        return self.stack[self.top]

    def display(self):

        if self.isempty():
            print('The stack is empty')
            return

        print('The elements in the stack are:')

        print('-----------------------------')

        for i in range(self.top, -1, -1):
            print(f'\t{self.stack[i]}')

        print('-----------------------------')


n = int(input('Get me the no. of inputs:\t'))

quad = Stack(capacity=n)

while True:

    print('\n1. For pushing value')
    print('2. For popping the value')
    print('3. To know the peek value')
    print('4. To display the stack elements')
    print('5. To return')

    x = int(input('Get me your choice:\t'))

    if x == 5:

        print('Thank you for choosing us.....')
        break

    elif x == 1:

        item = int(input('Get me the item to push:\t'))

        quad.push(item)

    elif x == 2:

        quad.pop()

    elif x == 3:

        print('The peek value in the stack is:\t', quad.peek())

    elif x == 4:

        print('Chosen to display all the elements in the stack:')
        quad.display()

    else:

        print('Entered some invalid stuff. Check again.')
