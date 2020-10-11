class Stack:
    def __init__(self, stack_length = 5):
        #attributes
        self.stack_length = stack_length
        self.stack = [None] * stack_length
        self.rear = -1
        self.front = -1




    def push(stack, input):
        if not self.isFull():
            if self.isEmpty():
                self.rear = 0
                self.front = 0
            else:
                self.rear += 1
            self.stack[self.rear] = input
            return True
        return False

    def pop(stack):
        if not self.isFull():
            popped = (stack[rear])
            stack.pop(rear)
            return (popped)
        else:
            return False

    def peek(stack):
        if not self.isEmpty():
            print(stack[rear])
            return True
        return False

    def isFull(self):
        if self.rear == self.stack_length:
            return True
        return False

    def isEmpty(self):
        if self.rear and self.front == -1:
            return True
        return False

Stack1 = Stack(6)
print(Stack1.get_stack_length())
print(Stack1.push(3))
