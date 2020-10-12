class Stack:
    def __init__(self, stack_length = 5):
        #attributes
        self.stack_length = stack_length
        self.stack = [None] * stack_length
        self.pointer = -1

    def isFull(self):
        if self.pointer == (self.stack_length - 1):
            return True
        return False

    def isEmpty(self):
        if self.pointer == -1:
            return True
        return False

    def push(self, input):
        if not self.isFull():
            self.pointer += 1
            self.stack[self.pointer] = input
            return True
        else:
            print("stack is full")
            return False

    def pop(self):
        if not self.isEmpty():
            popped = (stack[rear])
            stack.pop(rear)
            return (popped)
        else:
            print("stack is empty")
            return False

    def peek(self):
        if not self.isEmpty():
            print(stack[rear])
            return True
        print("stack is empty")
        return False



    def printing(self):
        if not self.isEmpty():
            print(self.stack)
            return True
        return False

Stack1 = Stack(6)
Stack1.pop()
Stack1.push(3)
Stack1.push(2)
Stack1.push(1)
Stack1.push(6)
Stack1.push(5)
Stack1.printing()
Stack1.push(7)
Stack1.push(4)
Stack1.printing()
