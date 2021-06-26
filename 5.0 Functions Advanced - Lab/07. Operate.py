def operate(operator,*args):
    if operator == '*' or operator == '/':
        result = 1
    else:
        result = 0
    for element in args:
        if operator =='+':
            result += element
        elif operator =='*':
            result *= element
        elif operator =='-':
            result-= element
        elif operator =='/':
            result /= element

    return result



