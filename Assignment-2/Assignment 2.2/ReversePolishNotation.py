import math

def ReversePolishNotation(tokens):
    stack = []

    for char in tokens:
        if char in {'+','-','*','/'} :
            num1 = stack.pop()
            num2 = stack.pop()

            if char == '+' : stack.append(num1 +  num2)
            elif char == '-': stack.append(num2 -  num1)
            elif char == '*': stack.append(num1 * num2)
            else: stack.append(int(num2 /  num1))
        else:
            stack.append(int(char))
    
    return stack.pop()

print(ReversePolishNotation(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))