class Stack
stack = []
def push(stack, input):
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

push(stack, 1)
