
PF1 = "0!!!1/10&1!!&=1=0|"
PF2 = "10=!10/&11!0/=1|11!&|&0/"

tos = ''

def push(stack, element):
    tempString = ""
    tempString += element
    length = len(stack)
    for i  in stack:
        tempString += i

    return list(tempString)


def pop(stack):
    global tos
    tos = stack[0]
    tempString = ""
    length = len(stack)
    for i in range(length):
        if i != 0:
            tempString += stack[i]
    return list(tempString)

#pop but doesn't set global variable
def remove(stack):
    top = stack[0]
    tempString = ""
    length = len(stack)
    for i in range(length):
        if i != 0:
            tempString += stack[i]
    return list(tempString), top

def logicalEval(expression):
    global tos
    tempStack = []
    stack = list(expression)

    while len(stack) > 0:
        stack = pop(stack)
        var = tos
        if tos == '!':
            tempStack, top = remove(tempStack)
            if top == '1':
                stack = push(stack, '0')
            elif top == '0':
                stack = push(stack, '1')
            else:
                print("! did not work")

        elif tos == '&':
            tempStack, top1 = remove(tempStack)
            tempStack, top2 = remove(tempStack)
            if (top1 == '1') and (top2 == '1'):
                stack = push(stack, '1')
            elif (top1 == '0') or (top2 == '0'):
                stack = push(stack, '0')
            else:
                print("& did not work")

        elif tos == '/':
            tempStack, top1 = remove(tempStack)
            tempStack, top2 = remove(tempStack)
            if top1 == top2:
                stack = push(stack, '0')
            elif top1 != top2:
                stack = push(stack, '1')
            else:
                print("/ did not work")

        elif tos == '=':
            tempStack, top1 = remove(tempStack)
            tempStack, top2 = remove(tempStack)
            if top1 == top2:
                stack = push(stack, '1')
            elif top1 != top2:
                stack = push(stack, '0')
            else:
                print("= did not work")

        elif tos == '|':
            tempStack, top1 = remove(tempStack)
            tempStack, top2 = remove(tempStack)
            if (top1 == '1') or (top2 == '1'):
                stack = push(stack, '1')
            elif (top1 == '0') and (top2 == '0'):
                stack = push(stack, '0')
            else:
                print("| did not work")

        else:
            tempStack = push(tempStack, tos)
    return tos


word = PF1
print("Input is " + word + " (PF1)."  "Expected result is 1. " +
                            "Actual result is: " + logicalEval(word))

word = PF2
print("Input is " + word + " (PF2)."  "Expected result is 1. " +
                            "Actual result is: " + logicalEval(word))

word = "01=1/10|1/&"
print("Input is " + word + "."  "Expected result is 0. " +
                            "Actual result is: " + logicalEval(word))

word = "11=0/0!&1|"
print("Input is " + word + "."  "Expected result is 1. " +
                            "Actual result is: " + logicalEval(word))

word = "10&11!&|0/"
print("Input is " + word + "."  "Expected result is 0. " +
                            "Actual result is: " + logicalEval(word))







