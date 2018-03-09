# !/usr/local/bin/python3


from pythonds.basic.stack import Stack


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    # postfixList = []
    digits = "0123456789"
    operators = "+-*/"

    for token in tokenList:
        if token.isdigit():
            operandStack.push(int(token))
        elif token in operators:
            secondOperand = operandStack.pop()
            firstOperand = operandStack.pop()
            # if token == operators[0]:
            #     Operand = firstOperand + secondOperand
            # elif token == operators[1]:
            #     Operand = firstOperand - secondOperand
            # elif token == operators[2]:
            #     Operand = firstOperand * secondOperand
            # elif token == operators[3]:
            #     Operand = firstOperand / secondOperand
            Operand = doMath(token, firstOperand, secondOperand)
            operandStack.push(Operand)

    assert(operandStack.size() == 1)
    res = operandStack.pop()
    return res


def doMath(op, fp, sp):
    if op == "+":
        Operand = fp + sp
    elif op == "-":
        Operand = fp - sp
    elif op == "*":
        Operand = fp * sp
    elif op == "/":
        Operand = fp / sp
    return Operand


print(postfixEval("70 8 +"))
print(postfixEval("17 10 + 3 * 9 /"))
