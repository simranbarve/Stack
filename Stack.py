class Stack:
    stack = []
    def __init__(self, stack_length = 5):
        #attributes
        self.__stack_length = stack_length

    #getters
    def get_stack_length(self):
        return self.__stack_length


    def push(stack, input):
        print(stack)
        stack = stack.append(input)
        print(input, "pushed to stack")

    def pop(stack):
        length = len(stack)
        if length == 0:
            print("stack is empty")
        else:
            popped = (stack[length-1])
            stack.pop(length - 1)
            print(stack)
            return(popped)

    def peek(stack):
        length = len(stack)
        if length == 0:
            print("stack is empty")
        else:
            print(stack[length-1])
        return length

    def isFull(self):
        length = len(stack)
        if length == self.__stack_length:
            print("stack is full")
        return length

    def isEmpty(self):
        length = len(stack)
        if length == 0:
            print("stack is empty")
        return length

Stack1 = Stack(6)
print(Stack1.get_stack_length())
print(Stack1.push(3))
